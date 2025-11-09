#!/usr/bin/env python3
from scapy.all import traceroute

res, unans = traceroute(["8.8.8.8"], maxttl=20)
res.show()
