import math

prime_num, prime_factors, n = [2], [], 600851475143
k = 3
j = 2
while k < round(math.sqrt(n)):
	if k % j == 0:
		k += 1
		j = 2
	elif round(math.sqrt(k)) + 1 == j:
		prime_num.append(k)
		k += 1
		j = 2
	j += 1

print(prime_num)	

while n != 1:
	for i in prime_num:
		if n % i == 0:
			n = n / i
			prime_factors.append(i)
			break

print(prime_factors)
largest = prime_factors[0]
for i in prime_factors:
	if i > largest:
		largest = i
print(largest)