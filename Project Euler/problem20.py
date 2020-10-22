n = 100
fact = 1
for i in range(n, 0, -1):
	fact *= i
print(fact)
sum = 0
while fact != 0:
	sum += fact % 10
	fact //= 10
	
print(sum)