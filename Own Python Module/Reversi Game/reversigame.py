from array1 import Array2D

class ReversiGameLogic:
	
	WHITE = 1
	BLACK = 0
	PLAYER1 = 1
	PLAYER2 = 2
	
	def __init__(self, whiteTuple, blackTuple):
		self._board = Array2D(8, 8)
		self._turn = 0
			
		for i in whiteTuple:
			row, col = i
			self._board[row, col] = ReversiGameLogic.WHITE
		
		for i in blackTuple:
			row, col = i
			self._board[row, col] = ReversiGameLogic.BLACK
			
	def __getitem__(self, ndxTuple):
		return self._board[ndxTuple[0], ndxTuple[1]]
		
	def __setitem__(self, ndxTuple, value):
		self._board[ndxTuple[0], ndxTuple[1]] = value
		
	def whoseTurn(self):
		if self._turn % 2 == 0:
			return ReversiGameLogic.PLAYER1
			
		elif self._turn % 2 == 1:
			return ReversiGameLogic.PLAYER2
		
		else:
			return 0
		
	def numChips(self, player):
		count = 0
		if player == ReversiGameLogic.PLAYER1:
			for i in range(8):
				for j in range(8):
					if self._board[i, j] == ReversiGameLogic.WHITE:
						count += 1
			return count
			
		if player == ReversiGameLogic.PLAYER2:
			for i in range(8):
				for j in range(8):
					if self._board[i, j] == ReversiGameLogic.BLACK:
						count += 1
			return count
			
	def getWinner(self):
		player1 = self.numChips(ReversiGameLogic.PLAYER1)
		player2 = self.numChips(ReversiGameLogic.PLAYER2)
		print("Player 1 has {} chips".format(player1))
		print("Player 2 has {} chips".format(player2))
		
		if  player1 > player2:
			return ReversiGameLogic.PLAYER1
			
		elif player2 > player1:
			return ReversiGameLogic.PLAYER2
		
		else:
			return 0
			
	def isLegalMove(self, row, col):
		cur = self.whoseTurn()
		valid = list()
		count = 0
		
		if cur == ReversiGameLogic.PLAYER1:
			for i in range(8):
				for j in range(8):
					if self._board[i, j] == ReversiGameLogic.WHITE:
						try:
							if self._board[i+1, j] == ReversiGameLogic.BLACK:
								if self._board[i+2, j] == '.':
									valid.append((i+2, j))	
						except AssertionError:
							pass
							
						try:
							if self._board[i-1, j] == ReversiGameLogic.BLACK:
								if self._board[i-2, j] == '.':
									valid.append((i-2, j))
						except AssertionError:
							pass
						
						try:
							if self._board[i, j+1] == ReversiGameLogic.BLACK:
								if self._board[i, j+2] == '.':
									valid.append((i, j+2))
						except AssertionError:
							pass
							
						try:
							if self._board[i, j-1] == ReversiGameLogic.BLACK:
								if self._board[i, j-2] == '.':
									valid.append((i, j-2))
						except AssertionError:
							pass
					
			for i in valid:
				if row == i[0] and col == i[1]:
					count = 1
			if count == 1:
				return True
			else:
				return False
			
		if cur == ReversiGameLogic.PLAYER2:
			for i in range(8):
				for j in range(8):
					if self._board[i, j] == ReversiGameLogic.BLACK:
						try:
							if self._board[i+1, j] == ReversiGameLogic.WHITE:
								if self._board[i+2, j] == '.':
									valid.append((i+2, j))	
						except AssertionError:
							pass
							
						try:
							if self._board[i-1, j] == ReversiGameLogic.WHITE:
								if self._board[i-2, j] == '.':
									valid.append((i-2, j))
						except AssertionError:
							pass
						
						try:
							if self._board[i, j+1] == ReversiGameLogic.WHITE:
								if self._board[i, j+2] == '.':
									valid.append((i, j+2))
						except AssertionError:
							pass
							
						try:
							if self._board[i, j-1] == ReversiGameLogic.WHITE:
								if self._board[i, j-2] == '.':
									valid.append((i, j-2))
						except AssertionError:
							pass
					
			for i in valid:
				if row == i[0] and col == i[1]:
					count = 1
			if count == 1:
				return True
			else:
				return False
		
	def occupiedBy(self, row, col):
		if self._board[row, col] == ReversiGameLogic.WHITE:
			return ReversiGameLogic.PLAYER1
			
		elif self._board[row, col] == ReversiGameLogic.BLACK:
			return ReversiGameLogic.PLAYER2
			
		else:
			return 0
			
	def numOpenSquares(self):
		count = 0
		for i in range(8):
			for j in range(8):
				if self._board[i, j] == '.':
					count += 1
		return count
		
	def makeMove(self, row, col):
		check = list()
		if self.isLegalMove(row, col):
			if self.whoseTurn() == ReversiGameLogic.PLAYER1:
				self._board[row, col] = ReversiGameLogic.WHITE
				
				try:
					if self._board[row-1, col-1] == ReversiGameLogic.BLACK and \
					   self._board[row-2, col-2] == ReversiGameLogic.WHITE:
						check.append((row-1, col-1))
				except AssertionError:
					pass
				
				try:
					if self._board[row-1, col] == ReversiGameLogic.BLACK and \
					   self._board[row-2, col] == ReversiGameLogic.WHITE:
						check.append((row-1, col))
				except AssertionError:
					pass
				
				try:
					if self._board[row-1, col+1] == ReversiGameLogic.BLACK and \
					   self._board[row-2, col+2] == ReversiGameLogic.WHITE:
						check.append((row-1, col+1))
				except AssertionError:
					pass
				
				try:
					if self._board[row, col-1] == ReversiGameLogic.BLACK and \
					   self._board[row, col-2] == ReversiGameLogic.WHITE:
						check.append((row, col-1))
				except AssertionError:
					pass
				
				try:
					if self._board[row, col+1] == ReversiGameLogic.BLACK and \
					   self._board[row, col+2] == ReversiGameLogic.WHITE:
						check.append((row, col+1))
				except AssertionError:
					pass
					
				try:
					if self._board[row+1, col-1] == ReversiGameLogic.BLACK and \
					   self._board[row+2, col-2] == ReversiGameLogic.WHITE:
						check.append((row+1, col-1))
				except AssertionError:
					pass
					
				try:
					if self._board[row+1, col] == ReversiGameLogic.BLACK and \
					   self._board[row+2, col] == ReversiGameLogic.WHITE:
						check.append((row+1, col))
				except AssertionError:
					pass
					
				try:
					if self._board[row+1, col+1] == ReversiGameLogic.BLACK and \
					   self._board[row+2, col+2] == ReversiGameLogic.WHITE:
						check.append((row+1, col+1))
				except AssertionError:
					pass
					
				for i in check:
					self._board[i[0], i[1]] = ReversiGameLogic.WHITE
			
			if self.whoseTurn() == ReversiGameLogic.PLAYER2:
				self._board[row, col] = ReversiGameLogic.BLACK
				
				try:
					if self._board[row-1, col-1] == ReversiGameLogic.WHITE and \
					   self._board[row-2, col-2] == ReversiGameLogic.BLACK:
						check.append((row-1, col-1))
				except AssertionError:
					pass
				
				try:
					if self._board[row-1, col] == ReversiGameLogic.WHITE and \
					   self._board[row-2, col] == ReversiGameLogic.BLACK:
						check.append((row-1, col))
				except AssertionError:
					pass
				
				try:
					if self._board[row-1, col+1] == ReversiGameLogic.WHITE and \
					   self._board[row-2, col+2] == ReversiGameLogic.BLACK:
						check.append((row-1, col+1))
				except AssertionError:
					pass
				
				try:
					if self._board[row, col-1] == ReversiGameLogic.WHITE and \
					   self._board[row, col-2] == ReversiGameLogic.BLACK:
						check.append((row, col-1))
				except AssertionError:
					pass
				
				try:
					if self._board[row, col+1] == ReversiGameLogic.WHITE and \
					   self._board[row, col+2] == ReversiGameLogic.BLACK:
						check.append((row, col+1))
				except AssertionError:
					pass
					
				try:
					if self._board[row+1, col-1] == ReversiGameLogic.WHITE and \
					   self._board[row+2, col-2] == ReversiGameLogic.BLACK:
						check.append((row+1, col-1))
				except AssertionError:
					pass
					
				try:
					if self._board[row+1, col] == ReversiGameLogic.WHITE and \
					   self._board[row+2, col] == ReversiGameLogic.BLACK:
						check.append((row+1, col))
				except AssertionError:
					pass
					
				try:
					if self._board[row+1, col+1] == ReversiGameLogic.WHITE and \
					   self._board[row+2, col+2] == ReversiGameLogic.BLACK:
						check.append((row+1, col+1))
				except AssertionError:
					pass
					
				for i in check:
					self._board[i[0], i[1]] = ReversiGameLogic.BLACK
					
			self._turn += 1

	def validDisplay(self):
		cur = self.whoseTurn()
		self.valid = list()
		
		if cur == ReversiGameLogic.PLAYER1:
			for i in range(8):
				for j in range(8):
					if self._board[i, j] == ReversiGameLogic.WHITE:
						try:
							if self._board[i+1, j] == ReversiGameLogic.BLACK:
								if self._board[i+2, j] == '.':
									self.valid.append((i+2, j))	
						except AssertionError:
							pass
							
						try:
							if self._board[i-1, j] == ReversiGameLogic.BLACK:
								if self._board[i-2, j] == '.':
									self.valid.append((i-2, j))
						except AssertionError:
							pass
						
						try:
							if self._board[i, j+1] == ReversiGameLogic.BLACK:
								if self._board[i, j+2] == '.':
									self.valid.append((i, j+2))
						except AssertionError:
							pass
							
						try:
							if self._board[i, j-1] == ReversiGameLogic.BLACK:
								if self._board[i, j-2] == '.':
									self.valid.append((i, j-2))
						except AssertionError:
							pass
					
			for i in self.valid:
				self._board[i[0], i[1]] = 'x'
			self.display()
			
		if cur == ReversiGameLogic.PLAYER2:
			for i in range(8):
				for j in range(8):
					if self._board[i, j] == ReversiGameLogic.BLACK:
						try:
							if self._board[i+1, j] == ReversiGameLogic.WHITE:
								if self._board[i+2, j] == '.':
									self.valid.append((i+2, j))	
						except AssertionError:
							pass
							
						try:
							if self._board[i-1, j] == ReversiGameLogic.WHITE:
								if self._board[i-2, j] == '.':
									self.valid.append((i-2, j))
						except AssertionError:
							pass
						
						try:
							if self._board[i, j+1] == ReversiGameLogic.WHITE:
								if self._board[i, j+2] == '.':
									self.valid.append((i, j+2))
						except AssertionError:
							pass
							
						try:
							if self._board[i, j-1] == ReversiGameLogic.WHITE:
								if self._board[i, j-2] == '.':
									self.valid.append((i, j-2))
						except AssertionError:
							pass
					
			for i in self.valid:
				self._board[i[0], i[1]] = 'x'
			self.display()

	def display(self):
		print("  ", end = '')
		for i in range(8):
			print(i, end = ' ')
		print()
		
		for i in range(8):
			print(i, end = ' ')
			for j in range(8):
				print(self[i, j], end = " ")
			print()
		print()
		print("Available Position to choose:")
		for i in self.valid:
			print(i[0] * 10 + i[1], end = ' ')
		print()
		
		for i in self.valid:
			self._board[i[0], i[1]] = '.'
			
			
	def isMoveAvailable(self):
		cur = self.whoseTurn()
		valid = list()
		
		if cur == ReversiGameLogic.PLAYER1:
			for i in range(8):
				for j in range(8):
					if self._board[i, j] == ReversiGameLogic.WHITE:
						try:
							if self._board[i+1, j] == ReversiGameLogic.BLACK:
								if self._board[i+2, j] == '.':
									valid.append((i+2, j))	
						except AssertionError:
							pass
							
						try:
							if self._board[i-1, j] == ReversiGameLogic.BLACK:
								if self._board[i-2, j] == '.':
									valid.append((i-2, j))
						except AssertionError:
							pass
						
						try:
							if self._board[i, j+1] == ReversiGameLogic.BLACK:
								if self._board[i, j+2] == '.':
									valid.append((i, j+2))
						except AssertionError:
							pass
							
						try:
							if self._board[i, j-1] == ReversiGameLogic.BLACK:
								if self._board[i, j-2] == '.':
									valid.append((i, j-2))
						except AssertionError:
							pass
					
			if len(valid) > 0:
				return True
			else:
				return False
			
		if cur == ReversiGameLogic.PLAYER2:
			for i in range(8):
				for j in range(8):
					if self._board[i, j] == ReversiGameLogic.BLACK:
						try:
							if self._board[i+1, j] == ReversiGameLogic.WHITE:
								if self._board[i+2, j] == '.':
									valid.append((i+2, j))	
						except AssertionError:
							pass
							
						try:
							if self._board[i-1, j] == ReversiGameLogic.WHITE:
								if self._board[i-2, j] == '.':
									valid.append((i-2, j))
						except AssertionError:
							pass
						
						try:
							if self._board[i, j+1] == ReversiGameLogic.WHITE:
								if self._board[i, j+2] == '.':
									valid.append((i, j+2))
						except AssertionError:
							pass
							
						try:
							if self._board[i, j-1] == ReversiGameLogic.WHITE:
								if self._board[i, j-2] == '.':
									valid.append((i, j-2))
						except AssertionError:
							pass
					
			if len(valid) > 0:
				return True
			else:
				return False
