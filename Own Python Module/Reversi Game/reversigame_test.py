from reversigame import ReversiGameLogic

listWhite = list()
listWhite.append((3,3))
listWhite.append((4,4))

listBlack = list()
listBlack.append((3,4))
listBlack.append((4,3))

new = ReversiGameLogic(listWhite, listBlack)

for i in range(8):
	for j in range(8):
		print(new[i, j], end = " ")
	print()
print()

new.makeMove(3, 5)
new.makeMove(2, 3)
new.makeMove(3, 2)
new.makeMove(4, 5)
new.makeMove(5, 5)
new.makeMove(3, 6)
new.makeMove(2, 5)
new.makeMove(5, 4)
new.makeMove(5, 3)
new.makeMove(6, 5)
new.makeMove(4, 6)
new.makeMove(5, 6)
new.makeMove(1, 3)

for i in range(8):
	for j in range(8):
		print(new[i, j], end = " ")
	print()
print()

while input("Is move available: ").capitalize() == "Y":
	if new.whoseTurn() == 1:
		print("Player 1 turn")
	elif new.whoseTurn() == 2:
		print("Player 2 turn")
	
	print("Enter the position")
	row, col = [int(x) for x in input().split()]
	new.makeMove(row, col)
	
	for i in range(8):
		for j in range(8):
			print(new[i, j], end = " ")
		print()

winner = new.getWinner()

if winner == ReversiGameLogic.PLAYER1:
	print("Player 1 won the game")
			
elif winner == ReversiGameLogic.PLAYER2:
	print("Player 2 won the game")
else:
	print("Match Draw")
