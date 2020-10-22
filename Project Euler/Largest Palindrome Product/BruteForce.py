reverse = 0
largest = 0
for i in range(999, 99, -1):
	for j in range(i, 99, -1):
		product = i * j
		copy = product
		while copy > 9:
			reverse += copy % 10
			reverse *= 10
			copy //= 10
		reverse += copy % 10
		if product == reverse:
			if largest < product:
				largest = product
		reverse = 0
		
print(largest)