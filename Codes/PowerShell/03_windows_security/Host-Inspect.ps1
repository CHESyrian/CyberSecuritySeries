# Phase-2 · Stage 3 — Windows host inspection helper
# Educational use only. Run on Windows lab VMs you control.
# Usage: .\Host-Inspect.ps1

Write-Output "=== Windows security-oriented inspection ==="
Write-Output "Date : $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Output "Host : $env:COMPUTERNAME"
Write-Output "User : $(whoami)"
Write-Output ""

Write-Output "--- Identity / groups ---"
whoami /groups 2>$null
Write-Output ""

Write-Output "--- Listening TCP connections ---"
try {
    Get-NetTCPConnection -State Listen -ErrorAction Stop |
        Select-Object LocalAddress, LocalPort, OwningProcess |
        Sort-Object LocalPort |
        Format-Table -AutoSize
} catch {
    Write-Output "(Get-NetTCPConnection unavailable; trying netstat)"
    netstat -ano | Select-String "LISTENING"
}
Write-Output ""

Write-Output "--- Top processes by CPU ---"
Get-Process |
    Sort-Object CPU -Descending |
    Select-Object -First 8 Name, Id, CPU, WorkingSet |
    Format-Table -AutoSize
Write-Output ""

Write-Output "--- Local Administrators group ---"
try {
    Get-LocalGroupMember -Group "Administrators" -ErrorAction Stop |
        Select-Object Name, ObjectClass, PrincipalSource |
        Format-Table -AutoSize
} catch {
    Write-Output "(Get-LocalGroupMember unavailable or access denied)"
}

Write-Output ""
Write-Output "Inspection complete. Record findings in your lab notebook."
Write-Output "SAFETY: Use only on laboratory systems you own or control."
