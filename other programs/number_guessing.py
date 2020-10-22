from random import randint

print('Guess a number between 1 to 100. You are given 10 guesses to find the right number')

print('Do you want to continue: Y/N', end=': ')

permit = input()

while permit.upper() == 'Y':
	turns = 10
	guessNum = randint(1, 100)
	while turns > 0:
		print()
		print('You have {} guess left'.format(turns))
		print()
		guess = int(input('Enter a number: '))
		
		if guess > guessNum:
			print('Your guess is too high')
		elif guess < guessNum:
			print('Your guess is too low')
		else:
			print('Congratulation, you find the number')
			break
			
		turns -= 1
		if turns == 0:
			print()
			print('Game Over')
	
	print()
	print('Do you want to play again: ', end='')
	permit = input()
	