print ("Enter any two values to find lcm: ")
first = int(input())
second = int(input())

if first > second:
	smallest_num = second
elif second > first:
	smallest_num = first
else:
	smallest_num = first

common_div = 1
i = 1

if smallest_num == first:
	if second % first == 0:
		lcm = second
	else:
		while i <= smallest_num:
			if first % i == 0 and second % i == 0:
				common_div = i
				
			i +=1

		if first / common_div == 1:
			lcm = second
		elif second / common_div == 1:
			lcm = first
		else:
			lcm = common_div * first / common_div * second / common_div		
		
else:
	if first % second == 0:
		lcm = first
	else:
		while i <= smallest_num:
			if first % i == 0 and second % i == 0:
				common_div = i

			i +=1
	
		if first / common_div == 1:
			lcm = second
		elif second / common_div == 1:
			lcm = first
		else:
			lcm = common_div * first / common_div * second / common_div

print ("LCM of two numbers {}" .format(lcm))
