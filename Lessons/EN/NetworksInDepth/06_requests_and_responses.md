# 06 — Requests and Responses in Detail

## Introduction

Most Internet application protocols follow a **request–response** pattern: a client sends a request message; a server returns a response message. HTTP is the dominant example and the focus of this module, but the same ideas appear in DNS, SMTP, API designs, and many proprietary protocols.

Understanding message structure, methods, status codes, and headers is required for web security, API work, traffic analysis, and troubleshooting.

---

## Learning Objectives

- Describe the structure of an HTTP request and response
- Explain common HTTP methods and their intended semantics
- Interpret status codes by class (1xx–5xx)
- Read and reason about important request and response headers
- Distinguish HTTP/1.1, HTTP/2, and HTTP/3 at a high level
- Relate request/response behaviour to security controls (TLS, headers, logging)

---

## Core Concepts

### 1. Generic Request–Response Model

```
Client                                Server
  |                                      |
  | -------- Request ------------------> |
  |                                      |
  | <------- Response ----------------- |
  |                                      |
```

Properties that vary by protocol:

- Synchronous vs asynchronous
- One request → one response vs streaming / multiplexing
- Textual vs binary framing
- Presence of intermediate proxies or caches

### 2. HTTP Request Structure (HTTP/1.1 style)

```
METHOD /path?query HTTP/1.1
Host: example.com
Header-Name: value
Another-Header: value

[optional body]
```

**Request line components:**

| Part | Meaning |
|------|---------|
| Method | Action (GET, POST, …) |
| Request-target | Path and optional query string |
| HTTP-version | Usually `HTTP/1.1` or implied by HTTP/2 framing |

**Common methods:**

| Method | Safe? | Idempotent? | Typical use |
|--------|-------|-------------|-------------|
| GET | Yes | Yes | Retrieve a resource |
| HEAD | Yes | Yes | Like GET but no body |
| POST | No | No | Submit data / create / action |
| PUT | No | Yes | Replace a resource |
| PATCH | No | No | Partial update |
| DELETE | No | Yes | Remove a resource |
| OPTIONS | Yes | Yes | Query supported methods / CORS preflight |

“Safe” means the method should not change server state. “Idempotent” means repeating the request has the same effect as doing it once.

### 3. HTTP Response Structure

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 1234
Header-Name: value

[body]
```

**Status line:** version + status code + reason phrase.

**Status code classes:**

| Class | Meaning | Examples |
|-------|---------|----------|
| 1xx | Informational | 100 Continue |
| 2xx | Success | 200 OK, 201 Created, 204 No Content |
| 3xx | Redirection | 301 Moved Permanently, 302 Found, 304 Not Modified |
| 4xx | Client error | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found |
| 5xx | Server error | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable |

### 4. Important Headers

**Request headers (selection):**

| Header | Role |
|--------|------|
| `Host` | Target host (required in HTTP/1.1); virtual hosting |
| `User-Agent` | Client identification string |
| `Accept` / `Accept-Language` / `Accept-Encoding` | Content negotiation |
| `Authorization` | Credentials (Basic, Bearer, …) |
| `Cookie` | Session / state cookies |
| `Content-Type` / `Content-Length` | Body description |
| `Origin` / `Referer` | Cross-origin and navigation context |
| `If-None-Match` / `If-Modified-Since` | Conditional requests / caching |

**Response headers (selection):**

| Header | Role |
|--------|------|
| `Content-Type` | Media type of the body |
| `Content-Length` / `Transfer-Encoding` | Body framing |
| `Set-Cookie` | Instruct client to store cookies |
| `Location` | Redirect target |
| `Cache-Control` / `ETag` / `Last-Modified` | Caching |
| `Strict-Transport-Security` | HSTS |
| `Content-Security-Policy` | XSS and injection mitigation |
| `X-Content-Type-Options` | MIME sniffing protection |
| `Access-Control-Allow-Origin` | CORS |

### 5. Bodies and Content Types

- Bodies may be empty (GET, HEAD, 204) or carry form data, JSON, XML, files, etc.
- `Content-Type` examples: `application/json`, `application/x-www-form-urlencoded`, `multipart/form-data`, `text/html`.
- Character encoding should be declared when relevant (`charset=utf-8`).

### 6. HTTP/2 and HTTP/3 (High Level)

| Version | Transport | Notable features |
|---------|-----------|------------------|
| HTTP/1.1 | TCP | Textual, one request at a time per connection (or pipelining with limits), head-of-line blocking |
| HTTP/2 | TCP | Binary framing, multiplexing, header compression (HPACK), server push (rarely used now) |
| HTTP/3 | QUIC (UDP) | Multiplexing without TCP head-of-line blocking, integrated TLS 1.3, faster connection establishment |

From a security analysis perspective you still see methods, paths, status codes, and headers; framing differs.

### 7. Proxies, Caches, and Intermediaries

- Forward proxies, reverse proxies, CDNs, and load balancers all sit in the request/response path.
- They may add headers (`X-Forwarded-For`, `Via`, `X-Request-ID`), terminate TLS, or cache responses.
- Understanding intermediaries is essential for interpreting logs and captures.

---

## Practical Examples

```bash
# Verbose HTTP request/response
curl -v https://example.com/

# Show response headers only
curl -I https://example.com/

# Custom method and headers
curl -X POST -H "Content-Type: application/json" \
     -d '{"name":"lab"}' https://httpbin.org/post

# Follow redirects and show the chain
curl -vL https://example.com/
```

Browser developer tools (Network tab) provide an interactive view of the same data.

---

## Common Mistakes

| Mistake | Issue |
|---------|-------|
| Treating all 4xx as “user error” and 5xx as “server error” without context | Proxies and WAFs can generate either; always inspect the body and logs |
| Ignoring security headers | Missing CSP, HSTS, etc. increases client-side risk |
| Assuming GET cannot change state | Poorly designed applications sometimes violate method semantics |
| Logging full Authorization or Cookie headers | Credential leakage in log systems |

---

## Best Practices

- Use TLS (HTTPS) for any non-public data.
- Prefer idempotent methods for safe retries.
- Set and review security-related response headers.
- Log method, path, status, timing, and a request ID; avoid logging secrets.
- In labs, practise reading raw requests/responses with `curl -v` and browser tools before relying on higher-level libraries.

---

## Hands-on Exercise

1. Issue a GET request with `curl -v` and identify the request line, at least five headers, the status line, and key response headers.
2. Send a POST with a JSON body and observe `Content-Type` and status code.
3. Trigger a redirect and list the status codes in the chain.
4. Compare an HTTP URL with its HTTPS counterpart (lab or public test sites only).
5. Inspect security headers on a chosen site (`Strict-Transport-Security`, `Content-Security-Policy`, etc.).

---

## Review Questions

1. What three components make up an HTTP request line?
2. Which status code class indicates success? Client error?
3. What is the difference between a safe method and an idempotent method?
4. Which header carries credentials in many API designs?
5. Why does HTTP/3 use QUIC over UDP instead of TCP?

---

## Summary

Request–response messaging is the backbone of web and API communication. HTTP methods, status codes, and headers carry both functional and security meaning. The ability to read raw messages is a core skill for developers, defenders, and analysts.

---

## Sources

- RFC 9110 (HTTP Semantics), RFC 9112 (HTTP/1.1), RFC 9113 (HTTP/2), RFC 9114 (HTTP/3)
- MDN Web Docs — HTTP
- OWASP guidance on security headers
