#used awk to get a text file of power usages
#script just adds them together and prints the total
with open ('./power_usage.txt', 'r') as power:
	total = 0
	for i in power:
		total += int(i.strip(''))
	print(total)
