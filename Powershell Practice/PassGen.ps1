#Defined lists
$upper = [char[]] (([char]'A')..([char]'Z'))
$lower = [char[]] (([char]'a')..([char]'z'))
$numbers = [char[]] (([char]'0')..([char]'9'))
$special = '!','@','#','$','%','^','&','*','(',')'
$total = $upper+$lower+$numbers+$special
#current list of passwords
$pass_csv = Import-Csv -Path .\new.csv


function Gen-Password {

#Prompt for password parameters with min length of 12
    $count = Read-Host -Prompt "How long would you like your password?"
    while ($count -lt 12){
        $count = Read-Host -Prompt "Password must be at least 12 characters. How long would you like your password?"
    }

#Generate password and save all characters as $test
    $password = Get-Random -InputObject $total -Count $count
    $test = ''
    foreach($i in $password){
        $test += $i
    }
    return $test
}

function New-Password {
    $pass = Gen-Password
    $test = Encrypt-String $pass
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
        $ct = Encrypt-String $user_pass

        $newpass = $pass_csv | where {$_.Website -eq $website}
        $newpass.Password = $ct
        $pass_csv | Export-Csv -NoTypeInformation -Path .\new.csv
    }
    if ($GenOrNah -eq "No"){
        $pass = Gen-Password
        $test = Encrypt-String $pass
        $existing_email = $pass_csv | where {$_.Website -eq $website}
        $existing_email.Password = $test
        $pass_csv| Export-Csv -NoTypeInformation -Path .\new.csv
    }
}

function Encrypt-String{
    param ($string)
    [Byte[]]$encodedBytes = [System.Text.Encoding]::UTF8.GetBytes($string)
    for($i=0; $i -lt $encodedBytes.count ; $i++){
        $encodedBytes[$i] = $encodedBytes[$i] -bxor 0x13
        }
    $encodedText = [System.Convert]::ToBase64String($encodedBytes)
    return $encodedText
}

function Decrypt-String{
    param ($ciphertext)
    [Byte[]]$DecodedText = [System.Convert]::FromBase64String($ciphertext)
    for($i = 0; $i -lt $DecodedText.count; $i++){
        $DecodedText[$i] = $DecodedText[$i] -bxor 0x13
        }
    $return = [System.Text.Encoding]::UTF8.GetString($DecodedText)
    return $return
}

function Check-Password{
    $prompt = Read-Host -Prompt "How do you want to lookup the password? Email or Website?"
    if ($prompt -eq "email"){
        $email = Read-Host -Prompt "What email do you want to lookup the password for?"
        $obj = $pass_csv | where {$_.Email -eq $email}
        $out = Select-Object -InputObject $obj -ExpandProperty Password
        $website = Select-Object -InputObject $obj -ExpandProperty Website
        $pt = Decrypt-String $out
        Write-Host "The password for $email on $website is $pt"
    }
    if ($prompt -eq "website"){
        $website = Read-Host -Prompt "What website do you want to lookup the password for?"
        $obj = $pass_csv | where {$_.Website -eq $website}
        $out = Select-Object -InputObject $obj -ExpandProperty Password
        $domain = Select-Object -InputObject $obj -ExpandProperty Website
        $pt = Decrypt-String $out
        Write-Host "The password for $email on $website is $pt"
    }
}

function Start-Main{
    $start = Read-Host -Prompt "What would you like to do? 1) Setup new account. 2) Change old password. 3) Check a password. 4) Exit Program."
    if ($start -eq 1){
        New-Password
    }
    if ($start -eq 2){
        Set-Password
    }
    if ($start -eq 3){
        Check-Password
    }
    if ($start -eq 4){
        exit
    }
    Start-Main
}

Start-Main