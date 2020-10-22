first, second, result, sum = 1, 2, 0, 0
array = [1, 2]
n = 100000
for i in range(2, n):
	sum = first + second
	first = second
	second = sum
	if sum < 40000000:
		array.append(sum)
	else:
		break
print(array)		
for i in range(1, len(array), 3):
	result += array[i]
print(result)