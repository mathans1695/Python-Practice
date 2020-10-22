prime_num, prime_factors, n = [2], [], 600851475143
for i in range(2, n+1):
	for j in range(2, i):
		if i % j == 0:
			break
		elif i == j + 1:
			prime_num.append(i)
		
while n != 1:
	for i in prime_num:
		if n % i == 0:
			n = n / i
			prime_factors.append(i)
		
largest = prime_factors[0]
for i in prime_factors:
	if i > largest:
		largest = i
print(largest)