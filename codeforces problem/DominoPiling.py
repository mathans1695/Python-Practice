m, n = map(int, input().split(' '))
arr = []
for i in range(m):
	new = []
	for j in range(n):
		new.append(0)
	arr.append(new)
	
place_holder = (1,1)

for i in range(len(arr)):
	for j in range(0, len(arr[0])-1, 2):
		arr[i][j], arr[i][j+1] = place_holder

for j in range(len(arr[0])):
	for i in range(0, len(arr)-1, 2):
		if arr[i][j] == 1:
			continue
		else:
			arr[i][j], arr[i+1][j] = place_holder
			
count = 0
for i in range(len(arr)):
	for j in range(len(arr[0])):
		if arr[i][j] == 1:
			count += 1

print(round(count/2))
