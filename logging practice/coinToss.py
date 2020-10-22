import random, logging, logging_practice

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(name)s:%(levelname)s:%(message)s')
fileHandler = logging.FileHandler('coinToss.log')
fileHandler.setFormatter(formatter)

streamHandler = logging.StreamHandler()
logger.addHandler(streamHandler)

logger.addHandler(fileHandler)

guess = ''
while guess not in ('heads', 'tails'):
	logger.debug('Guess the coin toss! Enter heads or tails:')
	guess = input()
	logger.debug('Guess = {}'.format(guess))

toss = random.randint(0, 1)
if toss == 0:
	toss = 'tails'
else:
	toss = 'heads'
	
logger.debug('toss = {}'.format(toss))
logger.debug('Checking toss and guess is equal')
logger.debug('Is it equal - {}'.format(toss == guess))
if toss == guess:
	logger.debug('You got it!')
else:
	logger.debug('Nope! Guess again!')
	guess = input()
	logger.debug('Another guess = {}'.format(guess))
	logger.debug('toss = {}'.format(toss))
	logger.debug('Checking toss and guess is equal')
	logger.debug('Is it equal - {}'.format(toss == guess))
	if toss == guess:
		logger.debug('You got it!')
	else:
		logger.debug('Nope. You are really bad at this game.')