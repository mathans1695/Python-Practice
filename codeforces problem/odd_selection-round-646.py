t = int(input())
result = []
for _ in range(t):
	n, x = [int(x) for x in input().split(' ')]
	arr = [int(x) for x in input().split(' ')]
	count = 0
	for i in range(0, len(arr)-x+1):
		sum, k = 0, i
		for j in range(x):
			sum += arr[k]
			k += 1
		if sum % 2 != 0:
			result.append('Yes')
			count = 1
			break
	if count != 1:
		result.append('No')
		
for i in result:
	print(i)