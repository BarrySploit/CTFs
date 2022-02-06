#Decided to bruteforce the code through python

#Variables from Assembly Code
xor_number = 1333337
add_number = 1337
sub_number = 133337

#This is the same process the Assembly puts our input through

for i in range(0000,99999999):
	
  #Convert to string and pad with leading zeros since input has to be at least 4 bytes (according to the assembly code)
  beginning = str(i).zfill(4)
  
  #convert back to int and start following the assembly
	first_step = int(beginning) ^ xor_number
	second_step = first_step + add_number
	third = second_step - sub_number
	#This is where it gets tricky. EAX * EAX * EAD basically means EAX * 3, don't get confused.
  fourth = third * 3
	#Another tricky EAX * 3.
  fifth = fourth * 3
  #EAX * EAX
	sixth = fifth * 2
  #Found out SAL means * 2 in this instance
  #https://c9x.me/x86/html/file_module_x86_id_285.html
	seventh = sixth * 2
  #check to see what makes the cmp intruction true!
	if seventh == 43270380:
		print(i)
