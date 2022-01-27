with open('./flaglist.txt', 'r') as flaglist:
	flag = []
	for i in flaglist:
		new = i.strip('\n')
		decode = bytes.fromhex(new).decode('utf-8')
		flag.append(decode)
	finalstring = ''
	for i in flag:
		finalstring += i
	print(finalstring)