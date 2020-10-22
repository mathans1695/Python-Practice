# Store last row and column as 1, as the last row and column will have one possible paths
# Next find the path of previous point in column wise and then row wise allocation can be done

row = 21
column = 21

list = []
for i in range(row):
	new = []
	for j in range(column):
		new.append(0)
	list.append(new)
	
for i in range(len(list)):
	list[i][len(list) - 1] = 1
	list[len(list) - 1][i] = 1
	
list[len(list) - 1][len(list) - 1] = 0
	
for i in range(len(list) - 2, -1, -1):
	for j in range(len(list[0]) - 2, -1, -1):
		list[i][j] = list[i + 1][j] + list[i][j + 1]
		
print(list[0][0])
		