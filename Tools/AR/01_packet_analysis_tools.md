# أدوات تحليل الحزم

تُستخدم في **المرحلة 2 — المرحلة 4** ومساري المرحلة 3 رقم 3 و5.

## Wireshark
| | |
|--|--|
| **ما هي** | محلل حزم رسومي |
| **الغرض** | رؤية حركة واجهة المختبر؛ مرشحات العرض؛ متابعة تدفقات TCP |

**شرح:** تلتقط الإطارات وتفكك البروتوكولات. مرشح العرض يحدّ ما تراه؛ مرشح الالتقاط يحدّ ما يُسجَّل.

**أمثلة (مختبر فقط):** اختر واجهة Host-Only؛ التقط أثناء تصفح تطبيق مختبر؛ مرشحات: `dns`، `http`، `tcp.port == 80`، `ip.addr == 192.168.56.10`؛ Follow TCP Stream.

## tshark
| | |
|--|--|
| **ما هي** | محرك Wireshark لسطر الأوامر |
| **الغرض** | التقاط بلا واجهة؛ ملخصات PCAP |

```bash
tshark -D
tshark -i eth0 -a duration:30 -w lab.pcap
tshark -r lab.pcap -c 20
tshark -r lab.pcap -Y "dns or http"
./Codes/Bash/04_network_analysis/tshark_quick_summary.sh lab.pcap
```

## Scapy (Python)
| | |
|--|--|
| **ما هي** | مكتبة Python لالتقاط/تشريح/بناء الحزم |
| **الغرض** | فهم بنية الحزمة؛ تجارب مختبر منضبطة |

```bash
python3 Codes/Python/04_network_analysis/read_pcap_scapy.py
python3 Codes/Python/04_network_analysis/sniff_packet_scapy.py
```
**سلامة:** لا تحقن حزماً على شبكات إنتاج أو الإنترنت العام.

## tcpdump
```bash
sudo tcpdump -i eth0 -n -c 50 -w lab_snap.pcap
```

## ping
```bash
ping -c 3 192.168.56.10
```


## سير عمل مختبري
1. أكد واجهة المختبر. 2. التقط بـ tshark/Wireshark. 3. ping وتصفح تطبيق المختبر. 4. احفظ PCAP. 5. `./Codes/Bash/04_network_analysis/tshark_quick_summary.sh lab.pcap`
