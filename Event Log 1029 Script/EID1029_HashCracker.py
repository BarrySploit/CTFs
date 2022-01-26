import hashlib
import base64

hash = input("What is the hash from the EID 1029 Event Log? (Ensure there are no extra spaces!) \n")
username_list = input("Enter path of list of usernames (ex: ./usernames.txt)\n")
with open(username_list, 'r') as wordlist:
    lines = wordlist.readlines()
    for line in lines:
        user = line.strip()
        username = hashlib.sha256(user.encode('utf-16-le')).digest()
        final = base64.b64encode(username)
        final_hash = final.decode('utf-8')
        if (final_hash) == hash:
            print('RESULTS FOUND:\n'+user+' is the username!')
        
