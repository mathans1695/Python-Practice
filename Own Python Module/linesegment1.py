from point1 import Point
import math

class LineSegment:
	def __init__(self, ptA, ptB):
		if ptA.getX() == ptB.getX():
			if ptA.getY() <= ptB.getY():
				self._pointA = ptA
				self._pointB = ptB
			else:
				self._pointA = ptB
				self._pointB = ptA
		
		elif ptA.getX() < ptB.getX():
			self._pointA = ptA
			self._pointB = ptB
		
		else:
			self._pointA = ptB
			self._pointB = ptA
	
	def endPointA(self):
		return "({}, {})".format(self._pointA.getX(), self._pointA.getY())
	
	def endPointB(self):
		return "({}, {})".format(self._pointB.getX(), self._pointB.getY())
		
	def __str__(self):
		return "({}, {})#({}, {})".format(self._pointA.getX(), self._pointA.getY(), \
											self._pointB.getX(), self._pointB.getY())
											
	def length(self):
		return Point.distance(self._pointA, self._pointB)
		
	def isVertical(self):
		if self._pointA.getX() == self._pointB.getX():
			return True
		return False
	
	def isHorizontal(self):
		if self._pointA.getY() == self._pointB.getY():
			return True
		return False
		
	def slopeptA(self):
		try:
			return (self._pointB.getY() - self._pointA.getY()) / (self._pointB.getX() - self._pointA.getX())
		except ZeroDivisionError:
			return "Infinity"
	
	def slopeptB(self):
		try:
			return (self._pointB.getY() - self._pointA.getY()) / (self._pointB.getX() - self._pointA.getX())
		except ZeroDivisionError:
			return "Infinity"
		
	def angle(self, otherLine):
		slopeA = self.slopeptA()
		slopeB = otherLine.slopeptB()
		
		try:
			temp = math.sqrt(((slopeB - slopeA) / (1 + slopeA * slopeB)) ** 2)
			angle = math.degrees(math.atan(temp))
			return angle
			
		except ZeroDivisionError:
			return 90
		
		except TypeError:
			if slopeA == 'Infinity':
				if slopeB == 0:
					return 90
				elif slopeB == 'Infinity':
					return 0
				else:
					angle = 90 - math.degrees(math.atan(slopeB))
					return angle
			
			else:
				if slopeA == 0:
					return 90
				else:
					angle = 90 - math.degrees(math.atan(slopeA))
					return angle
	
	def isParallel(self, otherLine):
		slopeA = self.slopeptA()
		slopeB = otherLine.slopeptB()
		
		if slopeA == slopeB:
			return True
		return False
	
	def isPerpendicular(self, otherLine):
		slopeA = self.slopeptA()
		slopeB = otherLine.slopeptB()
		
		try:
			if slopeA == -(1 / slopeB):
				return True
		except ZeroDivisionError:
			if self.isVertical():
				return True
		except TypeError:
			if slopeA == 0:
				return True
		return False
		
	def intersects(self, otherLine):
		slopeA = self.slopeptA()
		slopeB = otherLine.slopeptB()
		
		angle = self.angle(otherLine)
		
		if slopeA != slopeB:
			if angle != 90:
				return True
		return False
		
	def bisects(self, otherLine):
		slopeA = self.slopeptA()
		slopeB = otherLine.slopeptB()
		
		angle = self.angle(otherLine)
		
		if slopeA != slopeB:
			if angle == 90:
				x, y = self.intersectAtMidpoint(otherLine)
				tempA = self.midpoint()
				if (tempA.getX() == x) and (tempA.getY() == y):
					return True
				tempB = otherLine.midpoint()
				if (tempB.getX() == x) and (tempB.getY() == y):
					return True
		return False
	
	def slope(self):
		return "{}/{}".format(self._pointB.getY() - self._pointA.getY(), self._pointB.getX() - self._pointA.getX())
		
	def midpoint(self):
		return Point((self._pointB.getX() + self._pointA.getX()) / 2, (self._pointB.getY() + self._pointA.getY()) / 2)
	
	def intersectAtMidpoint(self, otherLine):
		slopeA = self.slopeptA()
		slopeB = otherLine.slopeptB()
		try:
			b1 = self._pointA.getY() - (slopeA * self._pointA.getX())
			b2 = otherLine._pointA.getY() - (slopeB * otherLine._pointA.getX())
			
			x = (b2 - b1) / (slopeA - slopeB)
			y = (slopeA * x) + b1
			
			return (x, y)
		
		except TypeError:
			if slopeA == 'Infinity':
				if slopeB == 0:
					return (self._pointA.getX(), otherLine._pointA.getY())
				else:
					return (100000, 100000)
			else:
				if slopeA == 0:
					return (otherLine._pointA.getX(), self._pointA.getY())
				else:
					return (100000, 100000)

