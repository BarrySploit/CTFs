import hashlib
with open('./passwords.txt', 'r') as passwords:
    passlist = []
    for i in passwords.readlines():
        passlist.append(str(i.strip("\n")))
    text = "SKY-HWZT-"
    for i in range(0,9999):
        begin = str(i).zfill(4)
        prehash = text+begin
        result = hashlib.md5(prehash.encode())
        if result.hexdigest() in passlist:
            print('PASSWORD FOUND: '+ prehash + "\nhash = " + result.hexdigest())
            
