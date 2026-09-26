# Track 1 · Stage 1.2 — Mapping and Proxy Workflow

## Why this stage matters
You cannot assess what you have not mapped. Systematic mapping reduces missed parameters and hidden authenticated surfaces.

## Learning objectives
- Build an anonymous vs authenticated site map for a lab app
- Configure an intercepting proxy **only** for lab traffic
- List interesting parameters and roles

## Safety checkpoint
Proxy listen address bound to local/lab interface. Scope limited to lab hostnames/IPs. Disable intercept when browsing unrelated sites.

## Core concepts
- Content discovery mindset (not brute-forcing the Internet)
- Spider/crawl with care on fragile lab apps
- Intercept → inspect → forward/drop
- Repeater-style manual request adjustment on lab targets

## Practice
1. Install/configure ZAP or Burp Community for lab only
2. Map Juice Shop or DVWA; export a simple sitemap
3. Note login-required areas and file upload or admin paths if present

## Review
- What is the difference between passive mapping and active discovery?
- Why must the proxy scope be restricted?
