#we know the flag prefix and just need a list to hash a list of possible flags
#Until we get a match for the given user hashes

#read list of user hashes
with open('./passwords.txt', 'r') as passwords:
    passlist = []
    for i in passwords.readlines():
        passlist.append(str(i.strip("\n")))
    text = "SKY-HWZT-"
    
#hash each possible flag until we find a match and print it out    
    for i in range(0,9999):
        begin = str(i).zfill(4)
        prehash = text+begin
        result = hashlib.md5(prehash.encode())
        if result.hexdigest() in passlist:
            print('PASSWORD FOUND: '+ prehash + "\nhash = " + result.hexdigest())
