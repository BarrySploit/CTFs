#challenge provides code that takes number higher than 47
#compares first four characters of sha256 hash against a12c
#this just bruteforces and prints out the numbers that it could be
#I'm sure I could consolidate some fo the lines in the loop, but it works so fuck it lol
import hashlib
key = "a12c"
for i in range(47, 1000000):
        test = str(i)
        encoded = test.encode()
        new = hashlib.sha256(encoded).hexdigest()
        if new[0:4] == key:
                print ("number = "+ str(i)+ " Hash = "+ str(new))
