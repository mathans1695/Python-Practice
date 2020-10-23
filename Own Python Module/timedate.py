from datetime import datetime

class TimeDate:

	def __init__(self, month = 0, day = 0, year = 0, hours = 0, minutes = 0, seconds = 0):
		if month == 0:
			month = datetime.now().date().month
		if year == 0:	
			year = datetime.now().date().year
		if day == 0:
			day = datetime.now().date().day
		if hours == 0:
			hours = datetime.now().time().hour
		if minutes == 0:	
			minutes = datetime.now().time().minute
		if seconds == 0:
			seconds = datetime.now().time().second
	
		assert self._isValidTime(hours, minutes, seconds), "Enter Valid Time"
		
		self._toSeconds = hours * 3600 + minutes * 60 + seconds
		
		assert self._isValidGregorian(month, day, year),  \
					"Invalid Gregorian date."
					
		tmp = 0
		if month < 3:
			tmp = -1
		self._julianDay = day - 32075 + \
				(1461 * (year + 4800 + tmp) // 4) + \
				(367 * (month - 2 - tmp * 12) // 12) - \
				(3 * ((year + 4900 + tmp) // 100) // 4)
				
	def hours(self):
		if self._toSeconds // 3600 == 24:
			return 0
		return self._toSeconds // 3600
		
	def seconds(self):
		return self._toSeconds % 60
		
	def minutes(self):
		return (self._toSeconds // 60) % 60
	
	def month(self):
		return (self._toGregorian())[0]
	
	def day(self):
		return (self._toGregorian())[1]
	
	def year(self):
		return (self._toGregorian())[2]
		
	def __str__(self):
		return "{:02}/{:02}/{:04} {:02}:{:02}:{:02}".format(self.month(), \
				self.day(), self.year(), self.hours(), self.minutes(), self.seconds())
				
	def __lt__(self, otherTime):
		if self._julianDay == otherTime._julianDay:
			return self._toSeconds < otherTime._toSeconds
		return self._julianDay < otherTime._julianDay
	
	def __le__(self, otherTime):
		if self._julianDay == otherTime._julianDay:
			return self._toSeconds <= otherTime._toSeconds
		return self._julianDay <= otherTime._julianDay		\
		
	def __eq__(self, otherTime):
		if self._julianDay == otherTime._julianDay:
			return self._toSeconds == otherTime._toSeconds
		return self._julianDay == otherTime._julianDay
		
	def _toGregorian(self):
		A = self._julianDay + 68569
		B = 4 * A // 146097
		A = A - (146097 * B + 3) // 4
		year = 4000 * (A + 1) // 1461001
		A = A - (1461 * year // 4) + 31
		month = 80 * A // 2447
		day = A - (2447 * month // 80)
		A = month // 11
		month = month + 2 - (12 * A)
		year = 100 * (B - 49) + year + A
		return month, day, year
	
	def _isValidTime(self, hours, minutes, seconds):
		if (0 <= hours <= 23) & (0 <= minutes <= 60) & (0 <= minutes <= 60):
			return True
		else:
			return False
	
	def _isValidGregorian(self, month, day, year):
		
		if (month % 2 != 0) & (1 <= month <= 12):
			if 1 <= day <= 31:
				if -4713 <= year <= 10000:
					return True
		
		elif (month % 2 == 0) & (1 <= month <= 12):
			if month == 2:
				if year % 100 == 0:
					if year % 400 == 0:
						if 1 <= day <= 29:
							if -4713 <= year <= 10000:
								return True
					else:
						return False
				
				elif year % 4 == 0:
					if 1 <= day <= 29:
						if -4713 <= year <= 10000:
							return True
				
				else:
					if 1 <= day <= 28:
						if -4713 <= year <= 10000:
							return True
		
			else:
				if 1 <= day <= 30:
					if -4713 <= year <= 10000:
						return True     
		return False
	
	def numDays(self, otherDate):
		if self._julianDay == otherDate._julianDay:
			return "{} seconds".format(abs(self._toSeconds - otherDate._toSeconds))
		else:
			return "{} days {} seconds".format(abs(self._julianDay - otherDate._julianDay), abs(self._toSeconds - otherDate._toSeconds))
	