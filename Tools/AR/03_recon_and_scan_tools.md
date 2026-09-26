# أدوات الاستطلاع والمسح (المختبر فقط)

في المرحلة 1 كمفاهيم؛ عملياً في المرحلة 2 — المرحلة 5. المسح غير المصرح به قد يكون غير قانوني.

## Nmap
| | |
|--|--|
| **ما هي** | ماسح اكتشاف الشبكة والمنافذ والخدمات |
| **الغرض** | جرد مضيفين وخدمات على **شبكة مختبرك فقط** |

```bash
nmap -sn 192.168.56.0/24
nmap -sS -sV -T3 --top-ports 100 192.168.56.10
./Codes/Bash/05_reconnaissance/safe_lab_nmap.sh 192.168.56.10
```

## ping
```bash
ping -c 3 192.168.56.10
```

## مساعدات Python socket (تعليمية)
```bash
python3 Codes/Python/05_reconnaissance/lab_port_scan.py 192.168.56.10
python3 Codes/Python/05_reconnaissance/lab_banner_grab.py 192.168.56.10 22
```
**سلامة:** عناوين مختبر فقط.


## سير عمل مختبري
```bash
./Codes/Bash/05_reconnaissance/safe_lab_nmap.sh 192.168.56.10
python3 Codes/Python/05_reconnaissance/lab_port_scan.py 192.168.56.10
```
فقط عناوين مختبرك.
