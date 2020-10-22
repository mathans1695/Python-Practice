#Counting Sundays

date1 = (1, 1, 1901)
date2 = (31, 12, 2000)

def isleap(i):
	if i % 100 and i % 4 == 0:
		return 29
	
	elif i % 4 == 0:
		return 29
		
	else:
		return 28

def day(days):
	dayname = days % 7
	
	if dayname == 0:
		return 'Sunday'
	elif dayname == 1:
		return 'Monday'
	elif dayname == 2:
		return 'Tuesday'
	elif dayname == 3:
		return 'Wednesday'
	elif dayname == 4:
		return 'Thursday'
	elif dayname == 5:
		return 'Friday'
	elif dayname == 6:
		return 'Saturday'
		
days = 366
count = 0
for i in range(date1[2], date2[2] + 1):
	for j in range(1, 13):
		if day(days) == 'Sunday':
			count += 1
			
		if j == 2:
			days += isleap(i)
		elif j == 4 or j == 6 or j == 9 or j == 11:
			days += 30
		else:
			days += 31

print(count)