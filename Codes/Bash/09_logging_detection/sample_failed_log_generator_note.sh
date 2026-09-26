#!/usr/bin/env bash
# Educational note: how to *safely* generate failed logons in a LAB for detection practice.
cat << 'EOF'
Generate lab-only failed logons (examples)
==========================================
Linux lab target (from attacker lab VM):
  ssh wronguser@192.168.56.10
  # repeat a few times intentionally; password will fail

Then on the target (or shared log):
  ./Codes/Bash/Track-2-SOC/count_auth_failures.sh /var/log/auth.log
  python3 Codes/Python/09_logging_detection/simple_detection_demo.py /var/log/auth.log -t 3

Windows lab: attempt a bad RDP/local logon only on your VM, then:
  Get-WinEvent ... Id 4625   or   .\Get-SecurityEvents.ps1 -LogonOnly

NEVER do this against systems you do not own.
EOF
