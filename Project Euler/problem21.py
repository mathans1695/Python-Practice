# Ambicable numbers
# Find the divisor of every numbers upto 10000 and sum it up
# Find the divisor of sum, then see if it is equal to the number
# If equal, add it to the result

result = 0
dict = {}
for i in range(1, 10000):
	if i in dict:
		result += i
		continue
		
	sum = 0
	for j in range(1, i):
		if i % j == 0:
			sum += j
	
	asum = 0
	for j in range(1, sum):
		if sum % j == 0:
			asum += j
	
	if asum == i:
		if sum == asum:
			pass
		else:
			result += i
			if sum > i:
				dict[sum] = sum
			print(i, sum, asum)
		
print(result)