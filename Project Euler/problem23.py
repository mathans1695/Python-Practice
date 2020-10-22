# Non - abundant sums
# Find the sum of divisor for each number 28123
# Add the abundant number in an array
import math, time

start = time.time()

abundant = []

for i in range(1, 28124):
	sum = 1
	for j in range(2, round(math.sqrt(i))+1):
		if i % j == 0:
			if j != i / j:
				div = i / j
				sum += j + div
			else:
				sum += j
			
	if sum > i:
		abundant.append(i)

sumabun = {}
count = 0
for i in abundant:
	if (i * 2) < 28123:
		sumabun[i * 2] = count
		count += 1
		
for i in range(0, len(abundant)):
	for j in range(i + 1, len(abundant)):
		if (abundant[i] + abundant[j]) < 28123:
			if (abundant[i] + abundant[j]) not in sumabun:
				sumabun[abundant[i] + abundant[j]] = count
				count += 1
			
file = open("sort1.txt", 'w')		
file.write("{}".format(sumabun))

result = 0
for i in range(1, 28123):
	if i not in sumabun:
		result += i
		
print(result)

print(time.time() - start)