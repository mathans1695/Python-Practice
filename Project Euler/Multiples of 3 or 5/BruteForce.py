sum = 0

# Iterate though every number and add the number to sum
# if multiples of 3 or 5
for i in range(1000):
	# Checks a number is divisible by 3 or 5
	if i % 3 == 0 or i % 5 == 0:
		sum += i
print(sum)