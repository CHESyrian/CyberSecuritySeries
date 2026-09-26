# أدوات التشفير والويب

## openssl
| | |
|--|--|
| **الغرض** | فحص شهادات X.509 وما يقدّمه خادم TLS |

```bash
openssl x509 -in lab.crt -noout -subject -issuer -dates
./Codes/Bash/08_cryptography/hash_and_cert_check.sh certfile lab.crt
./Codes/Bash/08_cryptography/hash_and_cert_check.sh cert 192.168.56.10:443
```

## sha256sum / hashlib
```bash
sha256sum file.bin
python3 Codes/Python/08_cryptography/hash_file.py file.bin
```

## أدوات مطوري المتصفح
افتح تطبيق المختبر → F12 → Network / Application → راقب الترويسات وملفات تعريف الارتباط.

## OWASP ZAP / Burp Community
| | |
|--|--|
| **الغرض** | وكيل اعتراض لتطبيقات **المختبر المقصودة فقط** |

اضبط المتصفح على الوكيل؛ قيّد النطاق بعنوان المختبر؛ عطّل الوكيل بعد التمرين.

## سكربتات المشروع
```bash
python3 Codes/Python/07_web/lab_http_observe.py http://192.168.56.10/dvwa/
python3 Codes/Python/Track-1-Web/check_security_headers.py http://192.168.56.10/
```


## سير عمل مختبري
```bash
./Codes/Bash/Track-1-Web/lab_curl_headers.sh http://192.168.56.10/
python3 Codes/Python/Track-1-Web/check_security_headers.py http://192.168.56.10/
python3 Codes/Python/08_cryptography/hash_file.py ./notes.txt
```
