from array1 import Array2D

class LifeGrid:
	
	DEAD_CELL = "."
	LIVE_CELL = "@"
	
	def __init__(self, numRows, numCols):
		self._grid = Array2D(numRows, numCols)
		self.configure(list())
		
	def numRows(self):
		return self._grid.numRows()
		
	def numCols(self):
		return self._grid.numCols()
		
	def configure(self, coordList):
		for i in range(self.numRows()):
			for j in range(self.numCols()):
				self.clearCell(i, j)
	
		for coord in coordList:
			self.setCell(coord[0], coord[1])
			
	def isLiveCell(self, row, col):
		return self._grid[row, col] == LifeGrid.LIVE_CELL
		
	def setCell(self, row, col):
		self._grid[row, col] = LifeGrid.LIVE_CELL
		
	def clearCell(self, row, col):
		self._grid[row, col] = LifeGrid.DEAD_CELL
		
	def numLiveNeighbors(self, row, col):
		neighbors = 0
		
		try:
			if self._grid[row-1, col-1] == LifeGrid.LIVE_CELL:
				neighbors += 1
		except AssertionError:
			pass
			
		try:
			if self._grid[row-1, col] == LifeGrid.LIVE_CELL:
				neighbors += 1
		except AssertionError:
			pass	
			
		try:
			if self._grid[row-1, col+1] == LifeGrid.LIVE_CELL:
				neighbors += 1
		except AssertionError:
			pass
			
		try:
			if self._grid[row, col-1] == LifeGrid.LIVE_CELL:
				neighbors += 1
		except AssertionError:
			pass
			
		try:
			if self._grid[row, col+1] == LifeGrid.LIVE_CELL:
				neighbors += 1
		except AssertionError:
			pass
			
		try:
			if self._grid[row+1, col-1] == LifeGrid.LIVE_CELL:
				neighbors += 1
		except AssertionError:
			pass
			
		try:
			if self._grid[row+1, col] == LifeGrid.LIVE_CELL:
				neighbors += 1
		except AssertionError:
			pass
		
		try:
			if self._grid[row+1, col+1] == LifeGrid.LIVE_CELL:
				neighbors += 1
		except AssertionError:
			pass
		return neighbors