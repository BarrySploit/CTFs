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
