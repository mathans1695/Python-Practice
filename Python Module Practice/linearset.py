class Set:
	def __init__(self, *initElements):
		self._theElements = list()
		for i in range(len(initElements)):
			self.add(initElements[i])
		
	def __len__(self):
		return len(self._theElements)
		
	def __contains__(self, element):
		return element in self._theElements
		
	def add(self, element):
		if element not in self:
			self._theElements.append(element)
			return True
			
	def remove(self, element):
		assert element in self, "The element must be in the set."
		self._theElements.remove(element)
		
	def __eq__(self, setB):
		if len(self) != len(setB):
			return False
		else:
			return self.isSubsetOf(setB)
			
	def __lt__(self, setB):
		for element in self:
			if element not in setB:
				return False
		return True
		
	def isProperSubset(self, setB):
		for element in self:
			if element not in setB:
				return False
		if len(self) != len(setB):
			return True
		return False
		
	def __add__(self, setB):
		newSet = Set()
		newSet._theElements.extend(self._theElements)
		for element in setB:
			if element not in self:
				newSet._theElements.append(element)
		return newSet
		
	def __mul__(self, setB):
		newSet = Set()
		for i in self:
			if i in setB:
				newSet.add(i)
		return newSet
	
	def __sub__(self, setB):
		newSet = Set()
		for i in self:
			if i not in setB:
				newSet.add(i)
		return newSet
		
	def __str__(self):
		temp = "{"
		for i in self._theElements:
			if i == self._theElements[len(self._theElements) - 1]:
				temp += '{}'.format(i)
			else:
				temp += "{}, ".format(i)
		temp += "}"
		return temp
		
	def __iter__(self):
		return _SetIterator(self._theElements)
		
class _SetIterator:
	def __init__(self, theSet):
		self._theRef = theSet
		self._count = 0
		
	def __iter__(self):
		return self
		
	def __next__(self):
		if self._count < len(self._theRef):
			item  =  self._theRef[self._count]
			self._count += 1
			return item
		else:
			raise StopIteration
				
