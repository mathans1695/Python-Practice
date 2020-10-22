# Solution obtained from swapping the rows and columns

arr = []
count = 0
for i in range(5):
	arr.append(list(map(int, input().split(' '))))
	
mid = (2, 2)
for i in range(5):
	for j in range(5):
		if arr[i][j] == 1:
			tuple = (i, j)
	
if tuple[0] < mid[0]:
	for i in range(tuple[0], mid[0]):
		swap = arr[i]
		arr[i] = arr[i+1]
		arr[i+1] = swap
		count += 1
		
elif tuple[0] > mid[0]:
	for i in range(tuple[0], mid[0], -1):
		swap = arr[i]
		arr[i] = arr[i-1]
		arr[i-1] = swap
		count += 1
		
if tuple[1] < mid[1]:
	for j in range(tuple[1], mid[1]):
		new = []
		temp = []
		for i in range(5):
			temp.append(arr[i][j])
		new.append(temp)
		temp = []
		for i in range(5):
			temp.append(arr[i][j+1])
		new.append(temp)
		
		swap = new[0]
		new[0] = new[1]
		new[1] = swap
		
		for k in range(0, 2):
			for i in range(5):
				arr[i][k+j] = new[k][i]
		count += 1

elif tuple[1] > mid[1]:
	for j in range(tuple[1], mid[1], -1):
		new = []
		temp = []
		for i in range(5):
			temp.append(arr[i][j])
		new.append(temp)
		temp = []
		for i in range(5):
			temp.append(arr[i][j-1])
		new.append(temp)
		
		swap = new[0]
		new[0] = new[1]
		new[1] = swap
		
		for k in range(0, 2):
			for i in range(5):
				arr[i][j-k] = new[k][i]
		count += 1

print(count)