with open("p067_triangle.txt", 'r') as file:
	data = file.read()

arr  = []
for i in data.split('\n'):
	arr.append(i.split(' '))
	
for i in range(len(arr)):
	for j in range(len(arr[i])):
		arr[i][j] = int(arr[i][j])
	
length = len(arr)
new = {}

for j in range(0, len(arr[length-2])):
	left = arr[length-2][j] + arr[length-1][j]
	right = arr[length-2][j] + arr[length-1][j+1]
	
	if left <= right:
		arr[length-2][j] = left
		new[(length-2, j)] = 'left'
	else:
		arr[length-2][j] = right
		new[(length-2, j)] = 'right'

for i in range(len(arr) - 3, -1, -1):
	for j in range(0, len(arr[i])):
		left = arr[i+1][j] + arr[i][j]
		right = arr[i+1][j+1] + arr[i][j]
		
		if left <= right:
			arr[i][j] = left
			new[(i, j)] = 'left'
		else:
			arr[i][j] = right
			new[(i, j)] = 'right'

i, j = 0, 0
path = [(0, 0)]
while length != 1:
	if new[(i, j)] == 'left':
		path.append((i+1, j))
		i += 1
		
	else:
		path.append((i+1, j+1))
		i += 1
		j += 1
		
	length -= 1

copy = arr
for i in range(len(copy)):
	for j in range(len(copy[i])):
		copy[i][j] = 0
		
for i in range(len(copy)):
	for j in range(len(copy[i])):
		if (i, j) in path:
			copy[i][j] = 1
		
for i in copy:
	print(i)