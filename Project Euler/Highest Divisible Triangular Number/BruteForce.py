import math

arr = [0]
sum = 0
for i in range(1, 20001):
	sum += i
	arr.append(sum)
	print(sum, end = ' ')

print(arr[len(arr)-1])

for i in range(2, len(arr)):
	count = 0
	for j in range(1, round(math.sqrt(arr[i]))+1):
		if arr[i] % j == 0:
			count += 2
			
	if count >= 500:
		print()
		print(arr[i])
		break


	
