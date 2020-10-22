import datetime

class Date:
  
  def __init__(self, month=0, day=0, year=0):
    self._julianDay = 0
    
    if month == 0:
      month = datetime.date.today().month
    if year == 0:	
      year = datetime.date.today().year
    if day == 0:
      day = datetime.date.today().day
    
    assert self._isValidGregorian(month, day, year),  \
                "Invalid Gregorian date."
    
    tmp = 0
    if month < 3:
      tmp = -1
    self._julianDay = day - 32075 + \
             (1461 * (year + 4800 + tmp) // 4) + \
             (367 * (month - 2 - tmp * 12) // 12) - \
             (3 * ((year + 4900 + tmp) // 100) // 4)
    
  def month(self):
    return (self._toGregorian())[0]
      
  def day(self):
    return (self._toGregorian())[1]
      
  def year(self):
    return (self._toGregorian())[2]
      
  def dayOfWeek(self):
    month, day, year = self._toGregorian()
    if month < 3:
      month = month + 12
      year = year - 1
    return ((13 * month + 3) // 5 + day + \
           year + year // 4 - year // 100 + year // 100) % 7
    
  def __str__(self):
    month, day, year = self._toGregorian()
    return "%02d/%02d/%04d" % (month, day, year)
    
  def __eq__(self, otherDate):
    return self._julianDay == otherDate._julianDay
    
  def __lt__(self, otherDate):
    return self._julianDay < otherDate._julianDay
    
  def __le__(self, otherDate):
    return self._julianDay <= otherDate._julianDay
    
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
    
  def _isValidGregorian(self, month, day, year):
    
    if 1 <= month <= 12:
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
      
      elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
         if 1 <= day <= 30:
           if -4713 <= year <= 10000:
             return True
      
      else:
          if 1 <= day <= 31:
           if -4713 <= year <= 10000:
             return True
    
    return False
  
  def monthName(self):
    month = self.month()
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
    else:
      return "December"
  
  def isLeapYear(self):
    year = self.year()
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    
    elif year % 4 == 0:
      return True
    
    else:
      return False
  
  def numDays(self, otherDate):
    return abs(self._julianDay - otherDate._julianDay)
  
  def dayOfWeekName(self):
    
    if self._julianDay % 7 == 0:
      return "Monday"
    elif self._julianDay % 7 == 1:
      return "Tuesday"
    elif self._julianDay % 7 == 2:
      return "Wednesday"
    elif self._julianDay % 7 == 3:
      return "Thursday"
    elif self._julianDay % 7 == 4:
      return "Friday"
    elif self._julianDay % 7 == 5:
      return "Saturday"
    elif self._julianDay % 7 == 6:
      return "Sunday"
  
  def dayOfYear(self):
    
    leap = self.isLeapYear()
    month = self.month()
    day = self.day()
    
    if not leap:
      if month == 1:
        return day
      elif month == 2:
        return 31 + day
      elif month == 3:
        return 59 + day
      elif month == 4:
        return 90 + day
      elif month == 5:
        return 120 + day
      elif month == 6:
        return 151 + day
      elif month == 7:
        return 181 + day
      elif month == 8:
        return 212 + day
      elif month == 9:
        return 243 + day
      elif month == 10:
        return 273 + day
      elif month == 11:
        return 304 + day
      elif month == 12:
        return 334 + day
    
    else:
      if month == 1:
        return day
      elif month == 2:
        return 31 + day
      elif month == 3:
        return 60 + day
      elif month == 4:
        return 91 + day
      elif month == 5:
        return 121 + day
      elif month == 6:
        return 152 + day
      elif month == 7:
        return 182 + day
      elif month == 8:
        return 213 + day
      elif month == 9:
        return 244 + day
      elif month == 10:
        return 274 + day
      elif month == 11:
        return 305 + day
      elif month == 12:
        return 335 + da
  
  def isWeekDay(self):
    
    weekday = self._julianDay % 7
    if 0 <= weekday <= 4:
      return True
    return False
  
  def isEquinox(self):
    
    day = self.day()
    month = self.month()
    
    if (month == 3) & (day == 20 | day == 21):
      return "Spring Equinox"
    
    elif (month == 9) & (day == 22 | day == 23):
      return "Autumn Equinox"
    
    else:
      return "Not an Equinox"
  
  def isSolstice(self):
    
    day = self.day()
    month = self.month()
    
    if (month == 6) & (day == 20 | day == 21):
      return "Summer Solstice"
    
    elif (month == 12) & (day == 21 | day == 22):
      return "Winter Solstice"
    
    else:
      return "Not an Solstice"  
  
  def asGregorian(self, divchar = '/'):
    
    month, day, year = self._toGregorian()
    return "{0:02}{1}{2:02}{3}{4:04}".format(month, divchar, day, divchar, year)
  
  def startDay(self):
    return self._julianDay % 7
  
new = Date()