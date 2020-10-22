import math

count = 2
i = 4

while count != 10001:
	for j in range(2, round(math.sqrt(i)) + 1):
		if i % j == 0:
			i += 1
			break
		elif j == round(math.sqrt(i)):
			count += 1
			i += 1
			
print(i-1)		