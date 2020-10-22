file = open('p022_names.txt', 'r')
data = file.read()
temp = data.split(',')
indiv_data = []
fi = open("sort.txt", 'w')

for i in temp:
	indiv_data.append(i[1:len(i)-1])
	
sorted_data = []

for i in range(0, len(indiv_data)):
	smallest = indiv_data[i]
	fi.write('{} {} '.format(i, smallest))
	
	for j in range(i + 1, len(indiv_data)):
		if indiv_data[j] < smallest:
			smallest = indiv_data[j]
			indies = j
	
	if smallest != indiv_data[i]:
		temp = indiv_data[i]
		indiv_data[i] = smallest
		indiv_data[indies] = temp
	
	fi.write('{}'.format(smallest))
	fi.write('\n')
	
dict = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16,'Q' : 17,'R' : 18,'S' : 19,'T' : 20,'U' : 21,'V' : 22,'W' : 23,'X' : 24,'Y' : 25,'Z' : 26}

result = 0
rs = [0]

for i in range(0, len(indiv_data)):
	sum = 0
	for j in range(0, len(indiv_data[i])):
		sum += dict[indiv_data[i][j]]
	
	rs.append(sum * (i + 1))
	
for i in rs:
	result += i
	
print(result)