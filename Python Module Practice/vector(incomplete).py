from array1 import Array

class Vector:
	def __init__(self):
		self._elements = Array(2)
		self._size = 2
		self._count = 1
	
	def __len__(self):
		return self._size
		
	def __contains__(self, item):
		return item in self._elements
		
	def __getitem__(self, ndx):
		assert 0 <= ndx < self._size, "List out of bound."
		return self._elements[ndx]
		
	def __setitem__(self, ndx, value):
		assert 0 <= ndx < self._size, "List out of bound."
		self._elements[ndx] = value
		
	def append(self, item):
		try:
			self._elements[len(self)] = item
			self._size += 1
		except AssertionError:
			self.doubleTheArray()
			self._elements[len(self)] = item
			self._size += 1
			
	def doubleTheArray(self):
		temp = Array(len(self) * 2)
		i = 0
		while i < self._size:
			temp[i] = self._elements[i]
			i += 1
			
		self._elements = temp
		self._count += 1
		
	def insert(self, ndx, item):
		assert 0 <= ndx < self._size, "List out of bound."
		self.shiftDown(ndx, item)
		self._elements[ndx] = item
		
	def shiftDown(self, ndx, item):
		size = self._size
		self.append(self._elements[size - 1])
		
		while size > ndx:
			if size == 1:
				break
			
			self._elements[size - 1] = self._elements[size - 2]
			size -= 1
	
	def remove(self, ndx):
		assert 0 <= ndx < self._size, "List out of bound."
		self.shiftUp(ndx)
		
	def shiftUp(self, ndx):
		p = ndx
		size = self._size
		if p == size - 1:
			self._elements[ndx] = None
			self._size -= 1
			return None
		
		while p < size:
			self._elements[p] = self._elements[p + 1]
			p += 1
		self._size -= 1
		
	def indexOf(self, item):
		for i in range(self._size):
			if item == self._elements[i]:
				return i
				break
				
	def extend(self, otherVector):
		for i in range(otherVector._size):
			self.append(otherVector[i])

	def subVector(self, from1, to):
		assert (0 <= from1 < self._size) and \
			(0 <= to < self._size), "List out of bound."
		temp = Vector()
		
		if to - from1 == 2:
			temp[0] = self._elements[from1]
			temp[1] = self._elements[to-1]
			return temp
		
		elif to - from1 == 1:
			temp[0] = self._elements[from1]
			temp._size -= 1
			return temp
			
		elif to - from1 == 0:
			temp._size -= 2
			return temp
			
		else:
			temp[0] = self._elements[from1]
			temp[1] = self._elements[from1 + 1]
			for i in range(2, to):
				temp.append(self._elements[i])
				
			return temp
			
	def reduce(self):
		print(self._size)
		if self._size == (2 ** (self._count - 1)):
			self._count -= 1
			
			temp = Array(2 ** self._count)
			i = 0
			while i < self._size:
				temp[i] = self._elements[i]
				i += 1
			
			self._elements = temp
	
	def __iter__(self):
		return _VectorIterator(self._elements)
		
class _VectorIterator:
	def __init__(self, theVector):
		self._theRef = theVector
		self._curNdx = 0
		
	def __iter__(self):
		return self
		
	def __next__(self):
		if self._curNdx < len(self._theRef):
			entry = self._theRef[self._curNdx]
			self._curNdx += 1
			return entry
		else:
			raise StopIteration
		
new = Vector()
new[0] = 1
new[1] = 2

for i in range(2, 5):
	new.append(i+1)

new.remove(0)
print(len(new))

print(new._count)