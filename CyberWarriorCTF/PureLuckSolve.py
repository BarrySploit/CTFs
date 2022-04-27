#CyberTalents PureLuck Reverse Engineering Challenge.
#Initial analysis showed the file was packed via UPX.
#Downloaded and ran upx-ucl to unpack it.
#Analyzed the new file in ghidra.
#Found main function.
#It adds random hex values to the stack and I added them to a file called flaglist.txt.
#Ran this script against it to return the flag.


#open file as flaglist variable
with open('./flaglist.txt', 'r') as flaglist:
	
	#add all values to list
	flag = []
	
	#strip unnecessary extras like \n. I manually deleted the 0x earlier.
	for i in flaglist:
		new = i.strip('\n')
		
		#convert hex bytes to ascii string
		decode = bytes.fromhex(new).decode('utf-8')
		flag.append(decode)
	
	#add each value in list to a string for easy copy and paste flag.
	finalstring = ''
	for i in flag:
		finalstring += i
	print(finalstring)
