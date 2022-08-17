$processes = reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options"
foreach ($i in $processes){
    $out = Get-Item -path registry::$i -ErrorAction Ignore
    if ($out.Property -contains "GlobalFlag"){
        Write-Host "Silent Exit Process detected!"
        $out.Name
        $process = Split-Path -Leaf $out.Name
        $reg = Get-ItemProperty -path registry::"HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\$process"
        Write-Host "When $process exits"$reg.MonitorProcess"will run"
        }
}
