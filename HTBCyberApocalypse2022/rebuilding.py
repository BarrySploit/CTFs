#Brute force the password
import re
import subprocess
import random
done = []
begin = ['htb{','htB{','hTb{','hTB{','Htb{','HtB{','HTb{','HTB{']

print(begin)

#Create list of all possible characters
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
all_char = []
for i in characters:
        all_char.append(i)
        all_char.append(i.upper())
all_char.append('_')

#Add numbers to the list
for i in range(0,10):
        all_char.append(i)

#create continuous loop that exits when answer is found
while 1==1:
        flag = ''
        x=0
        #Not including the htb{} we need 27 random characters, adds random characters until it meets that length
        while x != 27:
                z = random.randint(0,len(all_char)-1)
                flag += str(all_char[z])
                x += 1
		#path to patched binary, original binary had a sleep for 20 seconds function which I patched and removed via Ghidra
        cmd = '/home/remnux/malware/rev_rebuilding/rebuilding2'
		#Add the 27 characters to all htb{} combinations
        if flag in done:
                print('repeat')
        else:
                done.append(flag)
                for i in begin:
                        full_flag=i+flag+'}'
                        #run the binary with the potential flag as input and capture the output
                        output = subprocess.Popen([cmd, full_flag],stdout=subprocess.PIPE).communicate()
                	#search in output to see if flag is correct and print it out and quit the program if it is
                        match = re.search('password is correct',str(output[0]))
                        if match:
                               print(output)
                               print(full_flag)
                               quit()