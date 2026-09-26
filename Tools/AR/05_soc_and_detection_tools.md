# أدوات SOC والكشف

## سجلات Linux / journalctl
```bash
grep -iE 'failed|invalid' /var/log/auth.log | tail
./Codes/Bash/09_logging_detection/auth_failure_watch.sh
./Codes/Bash/Track-2-SOC/count_auth_failures.sh /var/log/auth.log
```

## سجل Security في Windows
```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624,4625} -MaxEvents 20
.\Codes\PowerShell\03_windows_security\Get-SecurityEvents.ps1 -LogonOnly
```

## SIEM مختبري
| | |
|--|--|
| **أمثلة** | Wazuh، Security Onion خفيف، مكدس ELK محلي |
| **الغرض** | بحث وارتباط وتصميم كشف في مختبر تستضيفه |

لا يكشف SIEM الهجمات تلقائياً؛ أنت تعرّف ما هو «مهم».

## مساعدات المشروع
```bash
python3 Codes/Python/09_logging_detection/simple_detection_demo.py /var/log/auth.log -t 5
python3 Codes/Python/Track-2-SOC/detection_threshold_demo.py
./Codes/Bash/10_incident_response/collect_basic_evidence.sh
```


## سير عمل مختبري
```bash
python3 Codes/Python/09_logging_detection/simple_detection_demo.py /var/log/auth.log -t 3
python3 Codes/Python/Track-2-SOC/triage_template.py
./Codes/Bash/10_incident_response/collect_basic_evidence.sh
```
