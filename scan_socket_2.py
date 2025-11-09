#!/usr/bin/env python3
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_port(ip, port, timeout=1.0):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
            return port, True
        except Exception:
            return port, False

def scan_ports_parallel(ip, ports, workers=100):
    open_ports = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(scan_port, ip, p) for p in ports]
        for fut in as_completed(futures):
            port, is_open = fut.result()
            if is_open:
                open_ports.append(port)
    return sorted(open_ports)

if __name__ == "__main__":
    ip = "192.168.1.1"
    ports = range(1, 1025)  # e.g., scan 1-1024
    open_ports = scan_ports_parallel(ip, ports)
    print("Open ports:", open_ports)
