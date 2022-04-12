#devices_practice.txt is a list of battery percentages from using awk to get only that element
#get average battery percentage by adding all values together and dividing by the total
with open('./devices_practice.txt', 'r') as devices:
    total = 0
    for i in devices:
        begin = i.strip("%\n")
        total += int(begin)
    final = total / 3907
