# Phase-2 · Stage 3 — Startup programs and running services snapshot
# Educational. Lab VMs only.
# Usage: .\Get-StartupAndServices.ps1

Write-Output "=== Startup (Run key) ==="
$runKey = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
try {
    Get-ItemProperty -Path $runKey -ErrorAction Stop |
        Select-Object * -ExcludeProperty PS* |
        Format-List
} catch {
    Write-Output "(Could not read $runKey)"
}

Write-Output ""
Write-Output "=== Running services (sample) ==="
try {
    Get-Service |
        Where-Object { $_.Status -eq 'Running' } |
        Select-Object -First 25 Name, DisplayName, Status, StartType |
        Format-Table -AutoSize
} catch {
    Write-Output "(Get-Service failed)"
}

Write-Output ""
Write-Output "=== Local users (names only) ==="
try {
    Get-LocalUser | Select-Object Name, Enabled, LastLogon | Format-Table -AutoSize
} catch {
    Write-Output "(Get-LocalUser unavailable)"
}

Write-Output ""
Write-Output "SAFETY: Lab systems only. Prefer read-only inspection while learning."
