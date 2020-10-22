a = 1
b = 1
count = 2
fib = 0
while fib < 10**999:
	fib = a + b
	a = b
	b = fib
	count += 1

print(count)	
