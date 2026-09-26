# أدوات البنية والسحابة

## فحص خط أساس المضيف
```bash
./Codes/Bash/02_linux_security/host_inspect.sh
./Codes/Bash/Track-3-Infra/baseline_ports_note.sh
```
```powershell
.\Codes\PowerShell\03_windows_security\Host-Inspect.ps1
```

## Nmap للجرد (مختبر)
```bash
./Codes/Bash/05_reconnaissance/safe_lab_nmap.sh 192.168.56.10
```

## جدار ناري / تجزئة
**الغرض:** تمرين عقلية الافتراضي-الرفض بين شرائح المختبر. جرّب فقط على بوابات تملكها؛ لقطة أولاً.

## مفاهيم IDS/IPS
فهم موضع الحساس والإيجابيات الكاذبة باستخدام PCAP أو حركة **مختبرية** — دون نشر على شبكات إنتاج.

## CLI السحابة (اختياري)
| | |
|--|--|
| **أمثلة** | AWS CLI، Azure CLI، gcloud |
| **الغرض** | فحص **مشاريعك** (مختبر/طبقة مجانية): الهوية، الشبكة، التخزين |

لا تستخدم حسابات إنتاج صاحب العمل. فعّل تنبيهات الفوترة إن وُجدت تكلفة. لا تمسح موارد مستأجرين آخرين.


## سير عمل مختبري
```bash
./Codes/Bash/Track-3-Infra/baseline_ports_note.sh
./Codes/Bash/05_reconnaissance/safe_lab_nmap.sh 192.168.56.10
```
السحابة: مشروعك فقط؛ أغلق الموارد المؤقتة بعد التمرين.
