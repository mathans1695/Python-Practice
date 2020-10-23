from date1 import Date

date = Date(10,6,1995)

def printCalendar(date):
	month = date.month()
	year = date.year()
	day = date.day()
	
	start_day = Date(month, 1, year).startDay()
	print(start_day)
	
	mY = date.monthName() + " " + str(date.year())
	print()
	print("{:^26}".format(mY))
	print("Su  Mo  Tu  We  Th  Fr  Sa", end = '')
	if start_day == 0:
		padding = 0
	padding = start_day * 4 + 4
	print(" " * padding, end = '')
	
	if (month == 4) or (month == 6) or (month == 9) or (month == 11):
		for i in range(30):
			if padding < 26:
				print("{:2}".format(i+1),end = "  ")
				padding += 4
				continue
			padding = 4
			print()
			print("{:2}".format(i+1),end = "  ")
			continue
	elif month == 2:
		if date.isLeapYear():
			for i in range(29):
				if padding < 26:
					print("{:2}".format(i+1),end = "  ")
					padding += 4
					continue
				padding = 4
				print()
				print("{:2}".format(i+1),end = "  ")
				continue
		else:
			for i in range(28):
				if padding < 26:
					print("{:2}".format(i+1),end = "  ")
					padding += 4
					continue
				padding = 4
				print()
				print("{:2}".format(i+1),end = "  ")
				continue
	else:
		for i in range(31):
			if padding < 26:
				print("{:2}".format(i+1),end = "  ")
				padding += 4
				continue
			padding = 4
			print()
			print("{:2}".format(i+1),end = "  ")
			continue
	
	print()

printCalendar(date)
