from array1 import Array2D

class GrayScaleImage:
	def __init__(self, nrows, ncols):
		self._elements = Array2D(nrows, ncols)
		self.clear(0)
	
	def width(self):
		return self._elements.numRows()
		
	def height(self):
		return self._elements.numCols()
		
	def clear(self, value):
		for i in range(self.width()):
			for j in range(self.height()):
				self._elements[i, j] = value
				
	def __getitem__(self, ndxTuple):
		return self._elements[ndxTuple[0], ndxTuple[1]]
	
	def __setitem__(self, ndxTuple, value):
		row, col = abs(ndxTuple[0]), abs(ndxTuple[1])
		while True:
			if row >= 255:
				row -= 255
				continue
			if col >= 255:
				col -= 255
				continue
			break
		self._elements[row, col] = value

