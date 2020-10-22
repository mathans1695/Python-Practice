n = 100000
first, second, result, sum = 1, 2, 2, 0
for i in range(1, n-1):
	sum = first + second
	first = second
	second = sum
	if i % 3 == 0 & sum < 40000000:
		result += sum
print(result)