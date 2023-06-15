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

function Invoke-Autoruns{
   #Check which computers are online
    $online_computers = @()
    foreach ($i in $computers){
        if (Test-Connection $i){
            $online_computers += $i
        }}
    
    #Copy Autorunsc64 to each online computer in the temp folder of the user profile being used to deploy the script
    foreach ($i in $online_computers){
        Write-Host "Copying Autorunsc to $i.";
        $temp_dst = invoke-command -ComputerName $i -ScriptBlock{ $env:temp -replace 'C:'}
        $dest = "\\"+$i+"\C$" + $temp_dst +"\autorunsc64.exe"
        Copy-Item -Path $fileshare_path -Destination $dest
        Write-Host "Copied."
        }
    #Execute Autoruns on each host and convert results to PS Object.    
    Write-Host "Executing Autorunsc on remote hosts. Please Wait."
    $output = Invoke-Command -ComputerName $online_computers -ScriptBlock {cd $env:TEMP; .\autorunsc64.exe -accepteula -a * -c -m * | Select-Object -Skip 5 | ConvertFrom-Csv -Delimiter ',';$autoruns}
    
    #Create array of objects
    #Deduplicate objects and add total number of occurances and which hosts they appear on
    $combined = @()
    foreach ($i in $output){
        if ($i.'Launch String'.length -eq 0){
            Continue
            }
        elseif ($i.'Launch String' -cnotin $combined.'Launch String'){
            Add-Member -InputObject $i -NotePropertyName Total -NotePropertyValue 1;
            $combined += $i
            }
        else {
            $x = $combined | Where-Object {$_.'Launch String' -eq $i.'Launch String'};
            if ($x.PSComputerName -inotlike $i.PSComputername){
                $x.PSComputerName += ("," + $i.PSComputerName)
                $x.total += 1
                }
            
        }}
    }
    #Write file to working directory
    $combined | ConvertTo-Csv | Out-File -FilePath .\Autoruns_Combined.csv | Write-Host "File has been written to Autoruns_Combined.csv"
    #Clean up/Remove Autorunsc64 from endpoints
    foreach ($i in $online_computers){
        Write-Host "Cleaning up $i."
        $temp_dst = invoke-command -ComputerName $i -ScriptBlock{ $env:temp -replace 'C:'}
        $dest = "\\"+$i+"\C$" + $temp_dst +"\autorunsc64.exe"
        Remove-Item $dest
        Write-Host "Cleaned up $i"
        }


Invoke-Autoruns
