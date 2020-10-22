
class Time:
	
	def __init__(self, hours = 0, minutes = 0, seconds = 0):
		
		assert self._isValidTime(hours, minutes, seconds), "Enter Valid Time"
		
		self._toSeconds = hours * 3600 + minutes * 60 + seconds
	
	def hours(self):
		if self._toSeconds // 3600 == 24:
			return 0
		return self._toSeconds // 3600
		
	def seconds(self):
		return self._toSeconds % 60
		
	def minutes(self):
		return (self._toSeconds // 60) % 60
		
	def numSeconds(self, otherTime):
		return abs(self._toSeconds - otherTime._toSeconds)
		
	def isAM(self):
		if 0 <= self.hours() < 12:
			return True
		return False
	
	def isPM(self):
		if 12 <= self.hours() < 24:
			return True
		return False
	
	def __lt__(self, otherTime):
		return self._toSeconds < otherTime._toSeconds
	
	def __le__(self, otherTime):
		return self._toSeconds <= otherTime._toSeconds
		
	def __eq__(self, otherTime):
		return self._toSeconds == otherTime._toSeconds
		
	def __str__(self):
		if 12 <= self.hours() < 13:
			return "{:02}:{:02}:{:02} PM".format(self.hours(),self.minutes(), self.seconds())
		
		elif 0 <= self.hours() < 1:
			return "{:02}:{:02}:{:02} AM".format(self.hours() + 12,self.minutes(), self.seconds())
			
		if 13 <= self.hours() < 24:
			return "{:02}:{:02}:{:02} PM".format(self.hours() - 12,self.minutes(), self.seconds())
		
		else:
			return "{:02}:{:02}:{:02} AM".format(self.hours(),self.minutes(), self.seconds())
		
			
	def _isValidTime(self, hours, minutes, seconds):
		if (0 <= hours <= 23) & (0 <= minutes <= 60) & (0 <= minutes <= 60):
			return True
		else:
			return False

