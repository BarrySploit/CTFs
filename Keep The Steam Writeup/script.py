import base64

#open strings.txt file that was extracted from decrypt-rm script
with open("./strings.txt", "r") as strings_file:
	#iterate through each base64 encoded HTTP response and decode
	for i in strings_file:
		decoded = base64.b64decode(i)
		#search for beginning of flag in each line
		if "HTB{" in str(decoded):

			#Display the base64 decoded HTTP response
			print(str(decoded))