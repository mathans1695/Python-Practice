data = 2 ** 1000
sum = 0

while data != 0:
	sum += data % 10
	data //= 10
	
print(sum)