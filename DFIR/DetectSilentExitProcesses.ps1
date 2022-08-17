#Used on endpoint to detect the presence of Silent Exit Processes. 
#A form of malware persistence that when a certain process exits, malware will run. 
#This script will detect and alert you to this form of persistence but will not delete it. This just gives you an IOC.

#Get list of processes with separate execution actions
$processes = reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options"
foreach ($i in $processes){
    $out = Get-Item -path registry::$i -ErrorAction Ignore
    #Silent Exit processes will contain the GlobalFlag option with 0x200
    if ($out.Property -contains "GlobalFlag"){
        Write-Host "Silent Exit Process detected!"
        $out.Name
        $process = Split-Path -Leaf $out.Name
        #Query SilentExitProcesses and return output
        $reg = Get-ItemProperty -path registry::"HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\$process"
        Write-Host "When $process exits"$reg.MonitorProcess"will run"
        }
}
