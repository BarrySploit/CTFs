#Defined lists
$upper = [char[]] (([char]'A')..([char]'Z'))
$lower = [char[]] (([char]'a')..([char]'z'))
$numbers = [char[]] (([char]'0')..([char]'9'))
$special = '!','@','#','$','%','^','&','*','(',')'
$total = $upper+$lower+$numbers+$special


function Gen-Password {

#Prompt for password parameters with min length of 12
    $count = Read-Host -Prompt "How long would you like your password?"
    while ($count -lt 12){
        $count = Read-Host -Prompt "Password must be at least 12 characters. How long would you like your password?"
    }

#Generate password and save all characters as $test
    $password = Get-Random -InputObject $total -Count $count
    Write-Host "This is your password!! with a length of $count!"
    $test = ''
    foreach($i in $password){
        $test += $i
    }
    $test2 = $test
    Write-Host $test
    return $test2
}

function New-Password {
    $test = Gen-Password
#Ask for additional info to store in password sheet
    $email = Read-Host -Prompt "What email is this associated with?"
    $domain = Read-Host -Prompt "What website is this used for?"
    $passobj =  New-Object psobject -Property @{
        'Email' = $email
        'Website' = $domain
        'Password' = $test
    }
#Add new password to password file/csv
    $passobj | Export-Csv -NoTypeInformation -Append -Force -Path .\new.csv
}

function Set-Password {
    $website = Read-Host -Prompt "What website are you wanting to change the password for?"
    $GenOrNah = Read-Host -Prompt "Are you using your own password? (Yes/No) 'No' will generate a new secure password for you!"
    if ($GenOrNah -eq "Yes"){
        $user_pass = Read-Host -Prompt "What is your password"
        $pass_csv = Import-Csv -Path .\new.csv
        $newpass = $pass_csv | where {$_.Website -eq $website}
        $newpass.Password = $user_pass
        $pass_csv | Export-Csv -NoTypeInformation -Path .\new.csv
    }
    if ($GenOrNah -eq "No"){
        $test = Gen-Password
        $pass_csv = Import-Csv -Path .\new.csv
        $existing_email = $pass_csv | where {$_.Website -eq $website}
        $existing_email.Password = $test
        $pass_csv| Export-Csv -NoTypeInformation -Path .\new.csv
    }
}
function Start-Main{
    $start = Read-Host -Prompt "What would you like to do? 1) Setup new account. 2) Change old password. 3) Exit Program."
    if ($start -eq 1){
        New-Password
    }
    if ($start -eq 2){
        Set-Password
    }
    if ($start -eq 3){
        exit
    }
    Start-Main
}

Start-Main
