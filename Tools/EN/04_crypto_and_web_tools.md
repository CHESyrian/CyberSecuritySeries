# Cryptography and Web Tools

Used in **Phase-2 Stages 7–8** and **Phase-3 Track 1**.

---

## openssl

| | |
|--|--|
| **What it is** | Toolkit for TLS/SSL, certificates, and related crypto operations |
| **Used for** | Inspecting X.509 certificates; viewing what a TLS service presents |

**Explanation:** Certificates bind identity information to public keys. `openssl` lets you read fields (subject, issuer, dates) from a file or from a live TLS handshake.

**Examples:**

```bash
# Certificate file
openssl x509 -in lab.crt -noout -subject -issuer -dates -fingerprint -sha256

# Passiveive view of a server certificate (lab or learning endpoint)
echo | openssl s_client -connect 192.168.56.10:443 -servername lab.local 2>/dev/null \
  | openssl x509 -noout -subject -issuer -dates
```

**Project helper:**

```bash
./Codes/Bash/08_cryptography/hash_and_cert_check.sh certfile lab.crt
./Codes/Bash/08_cryptography/hash_and_cert_check.sh cert 192.168.56.10:443
```

---

## sha256sum (and related)

| | |
|--|--|
| **What it is** | File hashing utility on Linux |
| **Used for** | Integrity checks — detect unexpected file changes in lab exercises |

**Examples:**

```bash
sha256sum important_file.bin
sha256sum important_file.bin > baseline.sha256
sha256sum -c baseline.sha256
```

Prefer SHA-256 (or stronger) for security-sensitive checks; MD5/SHA-1 are legacy.

---

## Python hashlib

| | |
|--|--|
| **What it is** | Standard library module for cryptographic hashes |
| **Used for** | Same integrity idea inside scripts |

**Example:**

```bash
python3 Codes/Python/08_cryptography/hash_file.py /path/to/file
python3 Codes/Python/08_cryptography/hash_file.py /path/to/file -a sha512
```

---

## Browser Developer Tools

| | |
|--|--|
| **What they are** | Built-in browser panels (Network, Application/Storage, Console) |
| **Used for** | Observing requests, cookies, redirects, and storage for **lab web apps** |

**Examples:**

1. Open lab app (e.g. `http://192.168.56.10/dvwa/`).  
2. F12 → **Network** → log in → inspect status codes, Set-Cookie, redirects.  
3. **Application** → Cookies → note `Secure` / `HttpOnly` if present.

---

## OWASP ZAP / Burp Suite Community

| | |
|--|--|
| **What they are** | Intercepting HTTP(S) proxies for security testing |
| **Used for** | Mapping and manually inspecting traffic to **intentional lab applications only** |

**Explanation:** The browser is configured to send traffic through the proxy. You can intercept, modify, and resend requests in a controlled lab.

**Example workflow:**

1. Start ZAP or Burp; set browser proxy to `127.0.0.1:8080` (or tool default).  
2. Restrict scope to lab hostname/IP.  
3. Browse DVWA/Juice Shop; map site; intercept a single lab request; forward.  
4. Disable proxy when finished so normal browsing is unaffected.

**Safety:** Never aim these tools at production or third-party sites without written authorization.

---

## lab_http_observe.py / check_security_headers.py

| | |
|--|--|
| **What they are** | Project Python helpers |
| **Used for** | Printing status/headers or security-related headers from a lab URL |

**Examples:**

```bash
python3 Codes/Python/07_web/lab_http_observe.py http://192.168.56.10/dvwa/
python3 Codes/Python/Track-1-Web/check_security_headers.py http://192.168.56.10/
```


---

## Worked lab workflow (web + crypto)

1. Open lab app; DevTools → Network; log in; save cookie flags.
2. Headers:
   ```bash
   ./Codes/Bash/Track-1-Web/lab_curl_headers.sh http://192.168.56.10/
   python3 Codes/Python/Track-1-Web/check_security_headers.py http://192.168.56.10/
   python3 Codes/Python/Track-1-Web/cookie_flags_note.py
   ```
3. Optional API peek (lab only):
   ```bash
   python3 Codes/Python/Track-1-Web/lab_api_get.py http://192.168.56.10/api/example
   ```
4. Hash a lab evidence file:
   ```bash
   python3 Codes/Python/08_cryptography/hash_file.py ./notes.txt
   ./Codes/Bash/08_cryptography/hash_and_cert_check.sh hash ./notes.txt
   ```

**Common mistakes**
- Pointing Burp/ZAP at the whole Internet proxy without scope.
- Confusing “missing security header” with remote code execution.
