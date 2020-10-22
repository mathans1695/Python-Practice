from math import sqrt

arr = []
sum = 0
for i in range(1, 100001):
	sum += i
	arr.append(sum)

for i in range(1, len(arr)):
	count = 2
	for j in range(2, round(sqrt(arr[i]))):
		if arr[i] % j == 0:
			count += 2
			
	if count > 500:
		print(arr[i])
		breakrth