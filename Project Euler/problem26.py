data = []
for i in range(20, 30):
	if 10 <= i < 100:
		data.append(str((1/i)*10))
	elif i >=100:
		data.append(str((1/i)*100))
	else:
		data.append(str(1/i))
	
for i in range(len(data)):
	data[i] = data[i].split('.')[1]
	
	index, count, j = 0, 0, 0
	while(j < len(data[i])-1):
		temp = data[i][j]
		if temp == data[i][j+1]:
			count += 1
		else:
			index = j
			
		j += 1
	print(count, data[i])