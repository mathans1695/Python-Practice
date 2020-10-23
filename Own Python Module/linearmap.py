from array1 import Array
import random
from linearset import Set

class Map:
	def __init__(self):
		self._entryList = list()
		
	def __len__(self):
		return len(self._entryList)
		
	def __contains__(self, key):
		ndx = self._findPosition(key)
		return ndx is not None
	
	def __setitem__(self, key, value):
		ndx = self._findPosition(key)
		if ndx is not None:
			self._entryList[ndx].value = value
			return False
		else:
			entry = _MapEntry(key, value)
			self._entryList.append(entry)
			return True
			
	def __getitem__(self, key):
		ndx = self._findPosition(key)
		assert ndx is not None, "Invalid map key."
		return self._entryList[ndx].value
		
	def remove(self, key):
		ndx = self._findPosition(key)
		assert ndx is not None, "Invalid map key."
		self._entryList.pop(ndx)
		
	def __iter__(self):
		return _MapIterator(self._entryList)
	
	def _findPosition(self, key):
		for i in range(len(self)):
			if key == self._entryList[i].key:
				return i
	
	def keyArray(self):
		temp = Array(len(self._entryList))
		numbers = Array(len(self._entryList))
		for i in range(len(numbers)):
			numbers[i] = i
		
		random.shuffle(numbers)
		
		for i in range(len(numbers)):
			temp[numbers[i]] = self._entryList[i].key
		return temp
				
class _MapEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value


class _MapIterator:
	def __init__(self, theMap):
		self._theRef = theMap
		self._count = 0
		
	def __iter__(self):
		return self
		
	def __next__(self):
		if self._count < len(self._theRef):
			key = self._theRef[self._count].key
			value = self._theRef[self._count].value
			self._count += 1
			return (key, value)
		else:
			raise StopIteration

new = Map()
new['super'] = 5
new[1] = 6
new[2] = 7

for i in new.keyArray():
	print(i)
