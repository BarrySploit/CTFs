import hashlib
key = "a12c"
for i in range(47, 1000000):
        test = str(i)
        encoded = test.encode()
        new = hashlib.sha256(encoded).hexdigest()
        if new[0:4] == key:
                print ("number = "+ str(i)+ " Hash = "+ str(new))