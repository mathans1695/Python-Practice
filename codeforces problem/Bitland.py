n = int(input())
count = 0
for i in range(n):
	statement = input()
	if statement == '++X' or statement == 'X++':
		count += 1
	else:
		count -= 1
		
print(count)