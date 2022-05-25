$knownhash = "6859e1d10d08c1ea91f6e53ba6d601149b08d4efab8f8c2d586f6858ae1773a7"
$directory = ls .\bin
foreach ($i in $directory){
    $hashes = Get-FileHash .\bin\$i
    if ($hashes.hash -eq $knownhash){
        $hashes
    }
}