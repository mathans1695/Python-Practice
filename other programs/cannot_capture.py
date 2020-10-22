def cannot_capture(board):
	try:
		print(board[8][0])
	except IndexError:
		pass
	i, j = (0, 0)
	while i < 8:
		j = 0
		while j < 8:
			if board[i][j] == 1:
				if 0 <= (j-2) < 8:
					if 0 <= (i-2) < 8:
						if board[i-1][j-2] == 1:
							return False
						elif board[i-2][j-1] == 1:
							return False
					if 0 <= (i+2) < 8:
						if board[i+2][j-1] == 1:
							return False
						elif board[i+1][j-2] == 1:
							return False
			
				if 0 <= (j+2) < 8:
					if 0 <= (i-2) < 8:
						if board[i-1][j+2] == 1:
							return False
						elif board[i-2][j+1] == 1:
							return False
					if 0 <= (i+2) < 8:
						if board[i+2][j+1] == 1:
							return False
						elif board[i+1][j+2] == 1:
							return False
			j += 1
		i += 1
	return True
		
		
print(cannot_capture([
[0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0],
[0, 1, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 1, 0, 0, 0]
]))