class Dict:
	def __init__(self):
		self._theItems = dict()
		self._numCopy = 1
	
	def __len__(self):
		return len(self._theItems)
	
	def __contains__(self, item):
		return item in self._theItems
	
	def add(self, item):
		if item in self._theItems:
			self._numCopy += 1
		self._theItems[item] = self._numCopy
	
	def grabItem(self):
		ndx = randrange(len(self._theItems))
		return self._theItems.pop(ndx)
		
	def remove(self, item):
		assert item in self._theItems, "The item must be in the bag"
		return self._theItems.pop(item)
		
	def display(self):
		return self._theItems
		
	def numOf(self, item):
		return self._theItems[item]
		
	def __iter__(self):
		return _BagIterators(self._theItems)
		
class _BagIterators:
	def __init__(self, theDict):
		self._bagItems = theDict
		self.count = 0
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.count < len(self._bagItems):
			key = list(self._bagItems.keys())[self.count]
			self.count += 1
			return key
			
		else:
			raise StopIteration

dic = Dict()
dic
print(dic)
