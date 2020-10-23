from reversigame import ReversiGameLogic

listWhite = list()
listWhite.append((3,3))
listWhite.append((4,4))

listBlack = list()
listBlack.append((3,4))
listBlack.append((4,3))

new = ReversiGameLogic(listWhite, listBlack)

print("  ", end = '')
for i in range(8):
	print(i, end = ' ')
print()

for i in range(8):
	print(i, end = ' ')
	for j in range(8):
		print(new[i, j], end = " ")
	print()
print()

while new.isMoveAvailable():
	if new.whoseTurn() == 1:
		print("Player 1 turn")
		print()
	elif new.whoseTurn() == 2:
		print("Player 2 turn")
		print()
	new.validDisplay()
	
	print("Enter the position:", end = ' ')
	inp = int(input())
	row, col = [inp // 10, inp % 10]
	new.makeMove(row, col)
	
	print("  ", end = '')
	for i in range(8):
		print(i, end = ' ')
	print()
	
	for i in range(8):
		print(i, end = ' ')
		for j in range(8):
			print(new[i, j], end = " ")
		print()
	print()

winner = new.getWinner()

if winner == ReversiGameLogic.PLAYER1:
	print("Player 1 won the game")
			
elif winner == ReversiGameLogic.PLAYER2:
	print("Player 2 won the game")
else:
	print("Match Draw")