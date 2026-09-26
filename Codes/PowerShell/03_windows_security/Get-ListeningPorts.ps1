# Phase-2 · Stage 3 — Map listening ports to processes
# Educational. Lab VMs only.
# Usage: .\Get-ListeningPorts.ps1

Write-Output "=== Listening ports → process map ==="
Write-Output "Host: $env:COMPUTERNAME  Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Output ""

try {
    $listeners = Get-NetTCPConnection -State Listen -ErrorAction Stop |
        Select-Object LocalAddress, LocalPort, OwningProcess

    foreach ($row in $listeners) {
        $proc = $null
        try {
            $proc = Get-Process -Id $row.OwningProcess -ErrorAction Stop
        } catch { }

        [PSCustomObject]@{
            LocalAddress  = $row.LocalAddress
            LocalPort     = $row.LocalPort
            PID           = $row.OwningProcess
            ProcessName   = if ($proc) { $proc.ProcessName } else { "?" }
            Path          = if ($proc) { $proc.Path } else { "" }
        }
    } | Sort-Object LocalPort | Format-Table -AutoSize
} catch {
    Write-Output "Falling back to netstat -ano"
    netstat -ano | Select-String "LISTENING"
}

Write-Output ""
Write-Output "Note: 0.0.0.0 / :: means all interfaces; 127.0.0.1 means localhost only."
