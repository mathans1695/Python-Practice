from date1 import Date

class ActivitiesCalendar:
	"""For creating activities within the specified fromdate and todate\n
	   Accepts fromdate and todate as arguments in the format of (mm/dd/yyyy) as string"""
	def __init__(self, dateFrom, dateTo):
		"""Accepts fromdate and todate as arguments in the format of mm/dd/yyyy as string"""
		self._theList = list()
		
		month, day, year = [int(x) for x in dateFrom.split('/')]
		self._dateFrom = Date(month, day, year)
		
		month, day, year = [int(x) for x in dateTo.split('/')]
		self._dateTo = Date(month, day, year)
		
		assert self._isValidDate(self._dateFrom, self._dateTo), "\nInvalid From and To date. The following may be the reasons:\n	1. Fromdate must precede Todate\n	2. Fromdate should not equal to Todate\n	3. Fromdate and Todate should not exceed a year"
		
		copy = self._dateFrom
		self._theList.append(copy)
		
		while copy != self._dateTo:
			try:
				copy = Date(copy.month(), copy.day() + 1, copy.year())
				self._theList.append(copy)
			except AssertionError:
				try:
					copy = Date(copy.month() + 1, 1, copy.year())
					self._theList.append(copy)
				except AssertionError:
					copy = Date(1, 1, copy.year() + 1)
					self._theList.append(copy)
		
		self._theDict = dict()
		
		for i in range(len(self._theList)):
			self._theDict["{:02}/{:02}/{:04}".format(self._theList[i].month(), self._theList[i].day(), self._theList[i].year())] = list()
		
	def addActivity(self, date, activity):
		"""To add activity to a particular date
		   Supply date and activity as arguments
		   Date in the format of mm/dd/yyyy
		   Both the arguments should be string
		   
		   returns added or failed"""
		month, day, year = [int(x) for x in date.split('/')]
		date = Date(month, day, year)
		
		if date in self._theList:
			self._theDict["{:02}/{:02}/{:04}".format(date.month(), date.day(), date.year())].append(activity)
			return "Added"
		return "Failed"
		
	def getActivity(self, date):
		"""returns list of activities for a particular date
		   Accepts date as argument in the format of mm/dd/yyyy as string"""
		month, day, year = [int(x) for x in date.split('/')]
		date = Date(month, day, year)
		
		if date in self._theList:
			activities = self._theDict["{:02}/{:02}/{:04}".format(date.month(), date.day(), date.year())]
			
			if len(activities) > 0:
				return activities
			else:
				return "No activities found"
		
		return "No activities found"
		
	def __len__(self):
		"""Returns the number of days which contains activities"""
		count = 0
		
		for key in self._theDict:
			if self._theDict[key] != []:
				count += 1
		if count != 0:
			return count
		return count
		
	def displayMonth(self, month):
		"""Display the activities of month on a day to day basis
		   Accepts month as argument as integer/number
		   return none"""
		print("{} {:04}\n".format(self.monthName(month), self._dateFrom.year()))
		
		list = ["{:02}/{:02}/{:04}".format(i.month(), i.day(), i.year()) for i in self._theList if i.month() == month]
		
		for i in list:
			if self._theDict[i] != []:
				print(i)
				print("", end='\t')
				for j in self._theDict[i]:
					print(j)
					print("", end='\t')
				print()
		
	def monthName(self, month):
		"""returns the corresponding month name"""
		if month == 1:
			return "January"
		elif month == 2:
			return "February"
		elif month == 3:
			return "March"
		elif month == 4:
			return "April"
		elif month == 5:
			return "May"
		elif month == 6:
			return "June"
		elif month == 7:
			return "July"	
		elif month == 8:
			return "August"
		elif month == 9:
			return "September"
		elif month == 10:
			return "October"
		elif month == 11:
			return "November"
		elif month == 12:
			return "December"
		else:
			return None
	
	def _isValidDate(self, dateFrom, dateTo):
		"""returns true or false
		   Validating calendar"""
		if dateFrom >= dateTo:
			return False
			
		elif  Date(dateFrom.month(), dateFrom.day(), dateFrom.year() + 1) == dateTo:
			return False
			
		else:
			return True				