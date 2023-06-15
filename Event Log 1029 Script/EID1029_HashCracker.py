#The EID1029 Script is meant to help find the username associated with the RDP Event Log ID 1029.
#In the Event Log, the username is encoded in UTF-16le and then hashed with SHA-256 then base64 encoded.
#We can't reverse a hash, but we can enumerate all the users from the device and compile them into a list. Ensure each username is on its own line and appended to a text file.
#The script will run each username through the same calculation that the Event Log does and compare the results.
#With a match, it will return the username associated with the Event Log ID.


import hashlib
import base64

#Prompt for Hash and Username list
hash = input("What is the hash from the EID 1029 Event Log? (Ensure there are no extra spaces!) \n")
username_list = input("Enter path of list of usernames (ex: ./usernames.txt)\n")

#Begin cracking
with open(username_list, 'r') as wordlist:
    lines = wordlist.readlines()
    for line in lines:
        user = line.strip()
        username = hashlib.sha256(user.encode('utf-16-le')).digest()
        final = base64.b64encode(username)
        final_hash = final.decode('utf-8')
        if (final_hash) == hash:
            print('RESULTS FOUND:\n'+user+' is the username!')
        
