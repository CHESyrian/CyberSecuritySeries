#!/usr/bin/env python3
import socket

def scan_port(ip, port, timeout=1.0):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False

if __name__ == "__main__":
    ip = "192.168.1.1"
    ports = [22, 80, 443, 8080]
    for p in ports:
        is_open = scan_port(ip, p)
        print(f"{ip}:{p} -> {'open' if is_open else 'closed'}")
