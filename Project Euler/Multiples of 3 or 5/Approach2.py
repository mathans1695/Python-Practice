sum = 0
# Iterating in steps of 3 upto 1000
for i in range(3, 1000, 3):
	# Omit the number which are divisible by 5
	if i % 5 == 0:
		continue
	sum += i

# Iterating in steps of 5 upto 1000
for i in range(5, 1000, 5):
	sum += i
print(sum)