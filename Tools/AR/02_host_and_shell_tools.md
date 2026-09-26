# أدوات المضيف وسطر الأوامر

## Bash
| | |
|--|--|
| **الغرض** | تشغيل أوامر وفحص المضيف على Linux المختبري |

```bash
whoami; id
ss -tulnp
./Codes/Bash/02_linux_security/host_inspect.sh
./Codes/Bash/02_linux_security/failed_logons_summary.sh
```

## ss / netstat
**الغرض:** سرد المنافذ والمقابس المستمعة.
```bash
ss -tulnp
```

## ps / top
**الغرض:** رؤية العمليات على مضيف المختبر.

## ip
```bash
ip -brief addr
```

## journalctl / auth.log
```bash
journalctl -u ssh -n 30 --no-pager
grep -iE 'failed|invalid' /var/log/auth.log | tail
python3 Codes/Python/02_linux_security/parse_auth_failures.py /var/log/auth.log
```

## PowerShell
| | |
|--|--|
| **الغرض** | فحص مضيف Windows المختبري والأحداث والخدمات |

```powershell
Get-NetTCPConnection -State Listen
Get-WinEvent -LogName Security -MaxEvents 15
.\Codes\PowerShell\03_windows_security\Host-Inspect.ps1
.\Codes\PowerShell\03_windows_security\Get-ListeningPorts.ps1
.\Codes\PowerShell\03_windows_security\Get-SecurityEvents.ps1 -LogonOnly
```

**معرفات شائعة للدراسة:** 4624 نجاح دخول، 4625 فشل دخول.


## سير عمل مختبري
```bash
./Codes/Bash/02_linux_security/host_inspect.sh
```
```powershell
.\Codes\PowerShell\03_windows_security\Host-Inspect.ps1
.\Get-ListeningPorts.ps1
```
