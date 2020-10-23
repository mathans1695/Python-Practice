import math

class Point:
	def __init__(self, x, y):
		self._xCoord = x
		self._yCoord = y
	
	def getX(self):
		return self._xCoord
	
	def getY(self):
		return self._yCoord
	
	def shift(self, xInc, yInc):
		self._xCoord += xInc
		self._yCoord += yInc
	
	def distance(self, otherPoint):
		xDiff = self._xCoord - otherPoint._xCoord
		yDiff = self._yCoord - otherPoint._yCoord
		return math.sqrt(xDiff ** 2 + yDiff ** 2)
		
	def __str__(self):
		return "({}, {})".format(self._xCoord, self._yCoord)