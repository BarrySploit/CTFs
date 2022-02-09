import requests
import re
import base64

url = "http://wcomk873ollhw3y05l3n94wbq36o0wz0mgrmfw3o-web.cybertalentslabs.com/index.php"

response = requests.get(url)
content = response.text
secret = re.findall('secret:(*)', content)[0]
print(secret)
decoded_secret = base64.b64decode(secret).decode('utf-8')
query = "Q:"+str(decoded_secret)

sonic_stomper = requests.get(url,params=query)
print(sonic_stomper)
