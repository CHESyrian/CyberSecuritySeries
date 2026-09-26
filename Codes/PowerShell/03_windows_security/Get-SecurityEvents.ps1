# Phase-2 · Stage 3 / 9 — Recent Security log events
# Educational. Requires permission to read the Security log.
# Usage: .\Get-SecurityEvents.ps1 [-MaxEvents 20] [-LogonOnly]

param(
    [int]$MaxEvents = 20,
    [switch]$LogonOnly
)

Write-Output "=== Windows Security events (newest first) ==="
Write-Output "Host: $env:COMPUTERNAME  MaxEvents: $MaxEvents"
Write-Output ""

try {
    if ($LogonOnly) {
        # 4624 success, 4625 failure
        Get-WinEvent -FilterHashtable @{LogName = 'Security'; Id = 4624, 4625} -MaxEvents $MaxEvents -ErrorAction Stop |
            Select-Object TimeCreated, Id, @{N = 'Message'; E = { $_.Message.Split("`n")[0] }} |
            Format-Table -AutoSize -Wrap
    } else {
        Get-WinEvent -LogName Security -MaxEvents $MaxEvents -ErrorAction Stop |
            Select-Object TimeCreated, Id, @{N = 'Message'; E = { $_.Message.Split("`n")[0] }} |
            Format-Table -AutoSize -Wrap
    }
} catch {
    Write-Output "Could not read Security log: $_"
    Write-Output "Try running elevated, or use: Get-EventLog -LogName Security -Newest $MaxEvents"
}

Write-Output ""
Write-Output "Common IDs: 4624=logon success, 4625=logon failure, 4672=special privileges, 4688=process create"
