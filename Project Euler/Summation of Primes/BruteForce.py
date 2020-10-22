import math

n = 2000000
sum = 5
for i in range(4, n):
	for j in range(2, round(math.sqrt(i)) + 1):
		if i % j == 0:
			break
		elif round(math.sqrt(i)) == j:
			sum += i
			
print(sum)