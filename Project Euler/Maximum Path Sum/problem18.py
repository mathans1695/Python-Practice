with open("p018_triangle.txt", 'r') as file:
	data = file.read()

arr  = []
for i in data.split('\n'):
	arr.append(i.split(' '))
	
for i in range(len(arr)):
	for j in range(len(arr[i])):
		arr[i][j] = int(arr[i][j])
	
length = len(arr)
for j in range(0, len(arr[length-2])):
	new = []
	new.append(arr[length-2][j] + arr[length-1][j])
	new.append(arr[length-2][j] + arr[length-1][j+1])
	arr[length-2][j] = new

for i in range(len(arr) - 3, -1, -1):
	for j in range(0, len(arr[i])):
		new = []
		for k in arr[i+1][j]:
			new.append(k + arr[i][j])
		for k in arr[i+1][j+1]:
			new.append(k + arr[i][j])
			
		arr[i][j] = new
			
for i in arr[0]:
	greatest = -1
	for j in i:
		if j > greatest:
			greatest = j
				
print(len(arr[0][0]), greatest)