# Initialize Greatest to zero
# Find the sequence from 2 to one million(inclusive)
# for i in range(2, 1000001)
# Assign i to j -> j = i
# Initialize count to zero
# Continue the loop until j becomes <1 or =1 -> while j >= 1:
# if j is even, divide j by and increment count by 1
# if j is odd, multiply j by 3 and add 1 to it and also increment count by 1
# After the loops gets over, check whether count is greater than greatest, if so assign greatest to i
# Atlast print greatest

from math import log

arr = [0,0]
greatest = 0
for i in range(2, 20):
	j = i
	count = 0
	print(j, end = ' ')
	
	while j > 1:
		if j < len(arr):
			count += arr[int(j)]
			j = 1
			break
			
		elif j % 2 == 0:
			j = j / 2
			count += 1
		else:
			j = 3 * j + 1
			count += 1
		print(j, end = ' ')
	print()
	
	if greatest < count:
		greatest = count
		temp = i
			
	arr.append(count)
	
for i in range(2, len(arr)):
	print(i, arr[i])
	
print(temp, greatest)