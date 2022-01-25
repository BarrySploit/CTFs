import hashlib
import base64

#Get User Input for list of usernames and hash from Event Log.
hash = input("What is the hash from the EID 1029 Event Log? (Ensure there are no extra spaces!) \n")
username_list = input("Enter path of list of usernames (ex: ./usernames.txt)\n")

#Open list of usernames
with open(username_list, 'r') as wordlist:
    lines = wordlist.readlines()
    
    #Iterate through list. Strip extra space, encode in utf-16le, make sha256 hash, and encode in base64.
    for line in lines:
        user = line.strip()
        username = hashlib.sha256(user.encode('utf-16-le')).digest()
        final = base64.b64encode(username)
        final_text = final.decode('utf-8')
        
        #Compare after calculations to see if it matches the encoded hash from the Event Log.
        if (final_text) == hash:
            print('RESULTS FOUND:\n'+user+' is the username!')
        
