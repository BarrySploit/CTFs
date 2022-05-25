#Given a hash, test all files in directory to find the file that has the same sha256 hash
$knownhash = "6859e1d10d08c1ea91f6e53ba6d601149b08d4efab8f8c2d586f6858ae1773a7"

#list out all files in directory
$directory = ls .\bin
#loop through each file and hash it and save to $hashes
foreach ($i in $directory){
    $hashes = Get-FileHash .\bin\$i
    #test if the hash property of the object is equal to knownhash (case insensitive)
    if ($hashes.hash -eq $knownhash){
        $hashes
    }
}
