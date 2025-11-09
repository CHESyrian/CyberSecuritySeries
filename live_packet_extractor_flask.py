#!/usr/bin/env python3
"""
live_packet_extractor_flask.py

Single-file Flask web app that captures network packets (using Scapy) and streams
extracted HTTP requests, DNS queries, and TLS SNI to a simple web UI in real-time
using Server-Sent Events (SSE).

Features:
- Start / Stop capture from the web UI
- Live streaming of extracted HTTP/DNS/SNI events to the browser
- Optionally analyze an existing pcap file (uploaded via the UI)
- Saves a JSON dump of extracted events per session

Requirements:
  pip install flask scapy
  Optional (for better TLS/HTTP dissection): pip install pyshark and install tshark

Notes:
- Must run with root/administrator privileges to capture live from network interfaces.
  On Linux: sudo python3 live_packet_extractor_flask.py
- On Windows: install Npcap and run as Administrator.
- This is a simple demo. For production use secure the endpoints and consider
  running packet capture as a separate privileged service.

Usage:
  sudo python3 live_packet_extractor_flask.py --iface eth0
  Then open http://127.0.0.1:5000 in your browser.

Note:
  This code had written by AI (ChatGPT)
"""

from flask import Flask, render_template_string, Response, request, jsonify
import threading
import time
import json
from collections import deque
import argparse

# Scapy imports
from scapy.all import sniff, wrpcap, rdpcap, IP, IPv6, TCP, UDP, Raw, DNS, DNSQR

# Try to import pyshark (optional)
try:
    import pyshark
    HAS_PYSHARK = True
except Exception:
    HAS_PYSHARK = False

app = Flask(__name__)

# Thread-safe queues to hold extracted events
EVENT_QUEUE = deque(maxlen=10000)  # events waiting to be sent to clients
CAPTURE_THREAD = None
CAPTURE_STOP = threading.Event()
CAPTURE_LOCK = threading.Lock()
CAPTURE_PACKETS = []  # store captured packets (optional, limited memory usage)
SESSION_RESULTS = {
    'http_requests': [],
    'dns_queries': [],
    'tls_sni': []
}

# Simple HTML template with JS EventSource for SSE and controls
HTML_TEMPLATE = '''
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Live Packet Extractor</title>
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial; padding: 20px; }
    .col { display:inline-block; vertical-align: top; width: 32%; margin-right:1%; }
    pre { background:#f6f6f6; padding:10px; border-radius:6px; height:300px; overflow:auto; }
    button { padding:8px 12px; margin-right:8px; }
  </style>
</head>
<body>
  <h2>Live Packet Extractor</h2>
  <div>
    <label>Interface: <input id="iface" value="{{ iface }}"></label>
    <button id="start">Start Capture</button>
    <button id="stop" disabled>Stop Capture</button>
    <button id="save">Save JSON</button>
    <label>Use pyshark: <input type="checkbox" id="use_pyshark"></label>
  </div>
  <hr>
  <div>
    <div class="col">
      <h3>HTTP Requests</h3>
      <pre id="http"></pre>
    </div>
    <div class="col">
      <h3>DNS Queries</h3>
      <pre id="dns"></pre>
    </div>
    <div class="col">
      <h3>TLS SNI</h3>
      <pre id="sni"></pre>
    </div>
  </div>

<script>
let evtSource = null;
const httpEl = document.getElementById('http');
const dnsEl = document.getElementById('dns');
const sniEl = document.getElementById('sni');
const startBtn = document.getElementById('start');
const stopBtn = document.getElementById('stop');
const saveBtn = document.getElementById('save');

function append(el, text){
  el.textContent = text + '\n' + el.textContent;
}

startBtn.onclick = async () => {
  const iface = document.getElementById('iface').value;
  const use_pyshark = document.getElementById('use_pyshark').checked ? '1' : '0';
  // request server to start capture
  const r = await fetch('/start?iface='+encodeURIComponent(iface)+'&use_pyshark='+use_pyshark,
    {method:'POST'});
  const data = await r.json();
  if(data.started){
    startBtn.disabled = true;
    stopBtn.disabled = false;
    // open SSE
    if(evtSource){ evtSource.close(); }
    evtSource = new EventSource('/stream');
    evtSource.onmessage = function(e){
      try{
        const obj = JSON.parse(e.data);
        if(obj.type === 'http'){
          append(httpEl, `[${new Date(obj.time*1000).toLocaleTimeString()}] ${obj.src} -> ${obj.host}${obj.uri} (${obj.method})`);
        } else if(obj.type === 'dns'){
          append(dnsEl, `[${new Date(obj.time*1000).toLocaleTimeString()}] ${obj.src} -> ${obj.query_name} (${obj.qtype})`);
        } else if(obj.type === 'sni'){
          append(sniEl, `[${new Date(obj.time*1000).toLocaleTimeString()}] ${obj.src} -> ${obj.sni}`);
        }
      }catch(err){ console.log('bad event', err); }
    };
    evtSource.onerror = function(e){ console.log('SSE error', e); };
  } else {
    alert('Failed to start capture: '+data.error);
  }
}

stopBtn.onclick = async () => {
  const r = await fetch('/stop', {method:'POST'});
  const data = await r.json();
  if(data.stopped){
    startBtn.disabled = false;
    stopBtn.disabled = true;
    if(evtSource){ evtSource.close(); evtSource = null; }
  }
}

saveBtn.onclick = async () => {
  const r = await fetch('/save', {method:'POST'});
  const data = await r.json();
  if(data.saved){
    alert('Saved JSON to: '+data.path);
  } else {
    alert('Save failed: '+(data.error||'unknown'));
  }
}
</script>
</body>
</html>
'''

# Extraction helpers (same logic as prior script)

def extract_from_scapy(pkt):
    evs = []
    # DNS
    try:
        if pkt.haslayer(DNS) and pkt.getlayer(DNS).qdcount > 0:
            for i in range(pkt[DNS].qdcount):
                q = pkt[DNS].qd[i]
                qname = q.qname.decode() if isinstance(q.qname, bytes) else str(q.qname)
                qtype = q.qtype
                ev = {
                    'type': 'dns',
                    'src': pkt[IP].src if pkt.haslayer(IP) else (pkt[IPv6].src if pkt.haslayer(IPv6) else None),
                    'query_name': qname.rstrip('.'),
                    'qtype': qtype,
                    'time': float(pkt.time)
                }
                evs.append(ev)
    except Exception:
        pass

    # HTTP (very simple)
    try:
        if pkt.haslayer(Raw) and pkt.haslayer(TCP):
            payload = bytes(pkt[Raw].load)
            for method in (b"GET", b"POST", b"PUT", b"DELETE", b"HEAD", b"OPTIONS", b"PATCH"):
                if payload.startswith(method + b" "):
                    try:
                        text = payload.split(b"\r\n\r\n", 1)[0].decode('utf-8', errors='ignore')
                        lines = text.splitlines()
                        request_line = lines[0] if lines else ""
                        parts = request_line.split(" ")
                        if len(parts) >= 2:
                            method_part = parts[0]
                            uri_part = parts[1]
                        else:
                            method_part = ''
                            uri_part = ''
                        host = ''
                        for line in lines[1:]:
                            if line.lower().startswith('host:'):
                                host = line.split(':',1)[1].strip()
                                break
                        ev = {
                            'type': 'http',
                            'src': pkt[IP].src if pkt.haslayer(IP) else (pkt[IPv6].src if pkt.haslayer(IPv6) else None),
                            'dst': pkt[IP].dst if pkt.haslayer(IP) else (pkt[IPv6].dst if pkt.haslayer(IPv6) else None),
                            'method': method_part,
                            'uri': uri_part,
                            'host': host,
                            'time': float(pkt.time)
                        }
                        evs.append(ev)
                    except Exception:
                        pass
                    break
    except Exception:
        pass

    return evs

# Capture worker using scapy

def scapy_capture_worker(iface=None, bpf=None, count=None, timeout=None, out_pcap=None):
    global CAPTURE_PACKETS
    CAPTURE_PACKETS = []

    def handler(pkt):
        # save packet memory-limited
        if len(CAPTURE_PACKETS) < 20000:
            CAPTURE_PACKETS.append(pkt)
        # extract events
        for ev in extract_from_scapy(pkt):
            SESSION_RESULTS['http_requests' if ev['type']=='http' else 'dns_queries'].append(ev)
            EVENT_QUEUE.append(ev)

    sniff_kwargs = dict(prn=handler, store=False)
    if iface:
        sniff_kwargs['iface'] = iface
    if bpf:
        sniff_kwargs['filter'] = bpf
    if count:
        sniff_kwargs['count'] = count
    if timeout:
        sniff_kwargs['timeout'] = timeout

    try:
        sniff(**sniff_kwargs, stop_filter=lambda x: CAPTURE_STOP.is_set())
    except Exception as e:
        EVENT_QUEUE.append({'type':'status','error':str(e),'time':time.time()})
    finally:
        # write pcap if requested
        if out_pcap and CAPTURE_PACKETS:
            try:
                wrpcap(out_pcap, CAPTURE_PACKETS)
            except Exception as e:
                EVENT_QUEUE.append({'type':'status','error':'pcap write failed: '+str(e),'time':time.time()})

# Pyshark live capture (optional, better for TLS SNI)

def pyshark_capture_worker(interface=None, bpf=None, count=None, timeout=None, out_pcap=None):
    # pylint: disable=unused-argument
    if not HAS_PYSHARK:
        EVENT_QUEUE.append({'type':'status','error':'pyshark not available','time':time.time()})
        return
    cap = pyshark.LiveCapture(interface=interface, bpf_filter=bpf)
    try:
        for pkt in cap.sniff_continuously(packet_count=count, timeout=timeout):
            # DNS
            try:
                if hasattr(pkt, 'dns') and getattr(pkt.dns, 'qry_name', None):
                    ev = {
                        'type': 'dns',
                        'src': getattr(pkt.ip, 'src', None),
                        'query_name': getattr(pkt.dns, 'qry_name', None),
                        'qtype': getattr(pkt.dns, 'qry_type', None),
                        'time': float(pkt.sniff_timestamp) if hasattr(pkt, 'sniff_timestamp') else time.time()
                    }
                    SESSION_RESULTS['dns_queries'].append(ev)
                    EVENT_QUEUE.append(ev)
            except Exception:
                pass
            # HTTP
            try:
                if hasattr(pkt, 'http') and hasattr(pkt.http, 'request_method'):
                    ev = {
                        'type':'http',
                        'src': getattr(pkt.ip, 'src', None),
                        'dst': getattr(pkt.ip, 'dst', None),
                        'method': getattr(pkt.http, 'request_method', None),
                        'uri': getattr(pkt.http, 'request_uri', None),
                        'host': getattr(pkt.http, 'host', None),
                        'time': float(pkt.sniff_timestamp) if hasattr(pkt, 'sniff_timestamp') else time.time()
                    }
                    SESSION_RESULTS['http_requests'].append(ev)
                    EVENT_QUEUE.append(ev)
            except Exception:
                pass
            # TLS SNI
            try:
                sni = None
                if hasattr(pkt, 'ssl') and hasattr(pkt.ssl, 'handshake_extensions_server_name'):
                    sni = pkt.ssl.handshake_extensions_server_name
                elif hasattr(pkt, 'tls') and hasattr(pkt.tls, 'handshake_extensions_server_name'):
                    sni = pkt.tls.handshake_extensions_server_name
                if sni:
                    ev = {
                        'type':'sni',
                        'src': getattr(pkt.ip, 'src', None),
                        'dst': getattr(pkt.ip, 'dst', None),
                        'sni': str(sni),
                        'time': float(pkt.sniff_timestamp) if hasattr(pkt, 'sniff_timestamp') else time.time()
                    }
                    SESSION_RESULTS['tls_sni'].append(ev)
                    EVENT_QUEUE.append(ev)
            except Exception:
                pass

            if CAPTURE_STOP.is_set():
                break
    except Exception as e:
        EVENT_QUEUE.append({'type':'status','error':'pyshark error: '+str(e),'time':time.time()})
    finally:
        cap.close()

# SSE stream endpoint
@app.route('/stream')
def stream():
    def event_stream():
        # keep connection open and yield events as they come
        while True:
            # if capture stopped and no pending events, break
            if not CAPTURE_THREAD or (not CAPTURE_THREAD.is_alive() and not EVENT_QUEUE):
                time.sleep(0.5)
                # still keep SSE alive until client closes
            try:
                if EVENT_QUEUE:
                    ev = EVENT_QUEUE.popleft()
                    # only send http/dns/sni and status
                    yield f'data: {json.dumps(ev, default=str)}\n\n'
                else:
                    time.sleep(0.2)
            except GeneratorExit:
                break
    return Response(event_stream(), mimetype='text/event-stream')

# Start capture endpoint
@app.route('/start', methods=['POST'])
def start_capture():
    global CAPTURE_THREAD
    if CAPTURE_THREAD and CAPTURE_THREAD.is_alive():
        return jsonify({'started': False, 'error': 'capture already running'})
    iface = request.args.get('iface')
    use_pyshark = request.args.get('use_pyshark', '0') == '1'
    # reset
    SESSION_RESULTS['http_requests'].clear()
    SESSION_RESULTS['dns_queries'].clear()
    SESSION_RESULTS['tls_sni'].clear()
    CAPTURE_STOP.clear()

    # start appropriate worker
    if use_pyshark and HAS_PYSHARK:
        t = threading.Thread(target=pyshark_capture_worker, kwargs={'interface': iface}, daemon=True)
    else:
        t = threading.Thread(target=scapy_capture_worker, kwargs={'iface': iface}, daemon=True)
    CAPTURE_THREAD = t
    t.start()
    EVENT_QUEUE.append({'type':'status','msg':'capture_started','time':time.time()})
    return jsonify({'started': True})

# Stop capture endpoint
@app.route('/stop', methods=['POST'])
def stop_capture():
    CAPTURE_STOP.set()
    # wait shortly for thread to stop
    if CAPTURE_THREAD:
        CAPTURE_THREAD.join(timeout=2)
    EVENT_QUEUE.append({'type':'status','msg':'capture_stopped','time':time.time()})
    return jsonify({'stopped': True})

# Save JSON endpoint
@app.route('/save', methods=['POST'])
def save_results():
    ts = int(time.time())
    path = f'extracted_{ts}.json'
    try:
        with open(path, 'w') as fh:
            json.dump(SESSION_RESULTS, fh, default=str, indent=2)
        return jsonify({'saved': True, 'path': path})
    except Exception as e:
        return jsonify({'saved': False, 'error': str(e)})

# Main page
@app.route('/')
def index():
    iface_default = 'eth0'
    return render_template_string(HTML_TEMPLATE, iface=iface_default)

# Analyze uploaded pcap (simple endpoint)
@app.route('/upload_pcap', methods=['POST'])
def upload_pcap():
    f = request.files.get('pcap')
    if not f:
        return jsonify({'ok': False, 'error': 'no file'})
    path = f"uploaded_{int(time.time())}.pcap"
    f.save(path)
    # analyze in background thread to avoid blocking
    def analyze_and_enqueue():
        analyze_pcap_file(path)
    threading.Thread(target=analyze_and_enqueue, daemon=True).start()
    return jsonify({'ok': True, 'path': path})

# Helper to analyze pcap file with scapy and push events
def analyze_pcap_file(path):
    try:
        pkts = rdpcap(path)
        for pkt in pkts:
            for ev in extract_from_scapy(pkt):
                SESSION_RESULTS['http_requests' if ev['type']=='http' else 'dns_queries'].append(ev)
                EVENT_QUEUE.append(ev)
    except Exception as e:
        EVENT_QUEUE.append({'type':'status','error': 'pcap analyze failed: '+str(e), 'time': time.time()})

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run live packet extractor web UI')
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=5000)
    parser.add_argument('--iface', default=None, help='Default interface shown in UI')
    args = parser.parse_args()
    # optionally change default iface in template
    if args.iface:
        HTML_WITH_IFACE = HTML_TEMPLATE.replace('{{ iface }}', args.iface)
        app.jinja_env.globals['iface'] = args.iface
    print('Starting Flask app — open http://127.0.0.1:5000')
    app.run(host=args.host, port=args.port, threaded=True)
