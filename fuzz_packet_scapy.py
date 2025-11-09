from scapy.all import send, IP, TCP, fuzz

for i in range(50):
    pkt = IP(dst="192.168.1.50")/TCP(dport=1234)/fuzz(b"payload")
    send(pkt, verbose=0)
