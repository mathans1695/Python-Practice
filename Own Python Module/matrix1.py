from array1 import Array2D

class Matrix:
	def __init__(self, numRows, numCols):
		self._theGrid = Array2D(numRows, numCols)
		self._theGrid.clear(0)
		
	def numRows(self):
		return self._theGrid.numRows()
		
	def numCols(self):
		return self._theGrid.numCols()
		
	def __getitem__(self, ndxTuple):
		return self._theGrid[ndxTuple[0], ndxTuple[1]]
		
	def __setitem__(self, ndxTuple, scalar):
		self._theGrid[ndxTuple[0], ndxTuple[1]] = scalar
		
	def scaleBy(self, scalar):
		for r in range(self.numRows()):
			for c in range(self.numCols()):
				self[r, c] *= scalar
				
	def tranpose(self):
		copy = Array2D(self.numCols(), self.numRows())
		for r in range(self.numRows()):
			for c in range(self.numCols()):
				copy[c, r] = self[r, c]
				
		return copy
		
	def __add__(self, rhsMatrix):
		assert rhsMatrix.numRows() == self.numRows() and \
			   rhsMatrix.numCols() == self.numCols(), \
			"Matrix sizes not compatible for the add operation."
		
		newMatrix = Matrix(self.numRows(), self.numCols())
		for r in range(self.numRows()):
			for c in range(self.numCols()):
				newMatrix[r, c] = self[r, c] + rhsMatrix[r, c]
		
		return newMatrix
		
	def __sub__(self, rhsMatrix):
		assert rhsMatrix.numRows() == self.numRows() and \
			   rhsMatrix.numCols() == self.numCols(), \
			"Matrix sizes not compatible for the sub operation."
		
		newMatrix = Matrix(self.numRows(), self.numCols())
		for r in range(self.numRows()):
			for c in range(self.numCols()):
				newMatrix[r, c] = self[r, c] - rhsMatrix[r, c]
		
		return newMatrix
		
	def __mul__(self, rhsMatrix):
		assert self.numCols() == rhsMatrix.numRows(), \
			"Matrix sizes not compatible for the mul operation"
			
		newMatrix = Matrix(self.numRows(), rhsMatrix.numCols())
		
		for r in range(self.numRows()):
			for c in range(rhsMatrix.numCols()):
				for k in range(rhsMatrix.numRows()):
					newMatrix[r, c] += self[r, k] * rhsMatrix[k, c]
		
		return newMatrix
				
new = Matrix(5,3)
rhsMatrix = Matrix(3, 5)

for i in range(new.numRows()):
	for j in range(new.numCols()):
		new[i, j] = 5
		
for i in range(rhsMatrix.numRows()):
	for j in range(rhsMatrix.numCols()):
		rhsMatrix[i, j] = 5

copy = new * rhsMatrix

for i in range(new.numRows()):
	for j in range(rhsMatrix.numCols()):
		print(copy[i, j], end = ' ')
	print()