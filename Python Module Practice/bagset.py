from bag import Bag

class Set:
	def __init__(self, *initElements):
		self._items = Bag()
		for i in initElements:
			self.add(i)
	
	def __len__(self):
		return len(self._items)
		
	def add(self, item):
		if item not in self:
			self._items.add(item)
			
	def remove(self, item):
		assert item in self, "Items not in the set"
		self._items._theItems.remove(item)
		
	def __lt__(self, setB):
		for item in self:
			if element not in setB:
				return False
		return True
		
	def isProperSubSet(self, setB):
		for item in self:
			if element not in setB:
				return False
		if len(self) != len(setB):
			return True
			
	def __eq__(self, setB):
		if len(self) !=  len(setB):
			return False
		return self.isSubSetOf(setB)
		
	def __add__(self, setB):
		new = Set()
		for i in self:
			new.add(i)
		for i in setB:
			new.add(i)
		return new
		
	def __sub__(self, setB):
		new = Set()
		for i in self:
			if i not in setB:
				new.add(i)
		return new
		
	def __mul__(self, setB):
		new = Set()
		for i in self:
			if i in setB:
				new.add(i)
		return new
			
	def __iter__(self):
		return _SetIterator(self._items)
		
class _SetIterator:
	def __init__(self, theRef):
		self._ref = theRef
		self.count = 0
		
	def __iter__(self):
		return self
		
	def __next__(self):
		if self.count < len(self._ref):
			item = self._ref._theItems[self.count]
			self.count += 1
			return item
		else:
			raise StopIteration