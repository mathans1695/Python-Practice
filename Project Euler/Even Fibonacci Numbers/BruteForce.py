n = 100
first, second, result, sum = 1, 2, 2, 0
for i in range(2, n):
	sum = first + second
	first = second
	second = sum
	if sum % 2 == 0:
		if sum < 4000000:
			result += sum
		else:
			break
print(result)