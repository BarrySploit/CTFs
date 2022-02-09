URL="http://wcomk873ollhw3y05l3n94wbq36o0wz0mgrmfw3o-web.cybertalentslabs.com/index.php"
curl -c /tmp/cookies.txt $URL
secret="$(grep -oP '(?<=secret)[^ ]*' /tmp/cookies.txt | xargs)"
final="${secret::-6}"
echo $final
decoded="$(echo $final|base64 -d)"
echo $decoded
curl $URL -b /tmp/cookies.txt -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' -H 'Cache-Control: max-age=0' --data-raw 'Q='$decoded''
