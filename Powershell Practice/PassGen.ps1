$count = Read-Host -Prompt "How long would you like your password?"
$upper = [char[]] (([char]'A')..([char]'Z'))
$lower = [char[]] (([char]'a')..([char]'z'))
$numbers = [char[]] (([char]'0')..([char]'9'))
$special = '!','@','#','$','%','^','&','*','(',')'
$total = $upper+$lower+$numbers+$special
$password = Get-Random -InputObject $total -Count $count
Write-Host "This is your password!! with a length of $count!"
$test = ''
foreach($i in $password){
    $test += $i
    }
$test
$password
$email = Read-Host -Prompt "What email is this associated with?"
$domain = Read-Host -Prompt "What website is this used for?"
$passobj =  New-Object psobject -Property @{
    'Email' = $email
    'Website' = $domain
    'Password' = $test
    }
$passobj | Export-Csv -Path .\test2.csv