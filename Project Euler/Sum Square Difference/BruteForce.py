sum = 0
sum1 = 0
n = 100
for i in range(1, n + 1):
	sum += i ** 2
	sum1 += i
	
sum1 *= sum1

print(abs(sum - sum1))