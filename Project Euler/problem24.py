str = '012'
count = 0

num_iter =  1
for i in range(len(str), 0, -1):
	num_iter *= i
	
while num_iter != 1:
	if num_iter % 2 != 0:
		temp = 