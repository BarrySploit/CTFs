#Find anomalies in autoruns output across org
#Uses PSRemoting to remotely execute autoruns

#Define these variables for your use

#Get list of computers using one of the two options below
#Option 1
#Uncomment the lines below to automatically pull computers from AD
#$computers = Get-ADComputer -Filter *
#Option 2
#OR Fill out specific computers here
$computers = @('Naboo','Endor','Tatooine','RebelallianceDC')

#Path to autoruns
$fileshare_path = "\\rebelalliancedc\adminshare\Sysinternals\autorunsc64.exe"
#\\rebelalliancedc\adminshare\Sysinternals\autorunsc64.exe -accepteula -c -s -m *

function Invoke-Autoruns{
    #test online computers
    $online_computers = @()
    foreach ($i in $computers){if (Test-Connection $i){$online_computers += $i}}
    foreach ($i in $online_computers){Write-Host "Copying Autorunsc to $i.";$dest = "\\"+$i+"\C$\Users\jasonbarry\autorunsc64.exe";Copy-Item -Path $fileshare_path -Destination $dest;Write-Host "Copied."}
    Write-Host "Executing Autorunsc on remote hosts. Please Wait."
    $output_csv = Invoke-Command -ComputerName $computers -ScriptBlock {C:\Users\jasonbarry\autorunsc64.exe -accepteula -a * -c -m * | Select-Object -Skip 5}
    $combined = @()
    $output = ConvertFrom-Csv -InputObject $output_csv -Delimiter ','
    foreach ($i in $output){if ($i.'Launch String'.length -eq 0){Continue}elseif ($i.'Launch String' -cnotin $combined.'Launch String'){Add-Member -InputObject $i -notepropertyname Total -notepropertyValue 1;$combined += $i}else {$x = $combined | Where-Object {$_.'Launch String' -eq $i.'Launch String'}; $x.total += 1}}
    $combined | ConvertTo-Csv 
    #clean up
    foreach ($i in $computers){Write-Host "Cleaning up $i.";$dest = "\\"+$i+"\C$\Users\jasonbarry\autorunsc64.exe";Remove-Item $dest;Write-Host "Cleaned up $i"}
}

Invoke-Autoruns