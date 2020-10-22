with open("p067_triangle.txt", 'r') as file:
	data = file.read()

arr  = []
for i in data.split('\n'):
	arr.append(i.split(' '))
	
for i in range(len(arr)):
	for j in range(len(arr[i])):
		arr[i][j] = int(arr[i][j])
	
length = len(arr)

for j in range(0, len(arr[length-2])):
	left = arr[length-2][j] + arr[length-1][j]
	right = arr[length-2][j] + arr[length-1][j+1]
	
	if left >= right:
		arr[length-2][j] = left
	else:
		arr[length-2][j] = right

for i in range(len(arr) - 3, -1, -1):
	for j in range(0, len(arr[i])):
		left = arr[i+1][j] + arr[i][j]
		right = arr[i+1][j+1] + arr[i][j]
		
		if left >= right:
			arr[i][j] = left
		else:
			arr[i][j] = right
							
print(arr[0][0])