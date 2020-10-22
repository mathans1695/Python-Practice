import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

fileHandler = logging.FileHandler('logging.log')

fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)

logger.debug('Start of program')

def factorial(n):
	logger.debug('Start of factorial(%s)' %(n))
	total = 1
	for i in range(1, n + 1):
		total *= i
		logger.debug('i is ' + str(i) + ', total is ' + str(total))
	logger.debug('End of factorial (%s)' %(n))
	return total
	
factorial(5)
	
logger.debug('End of program')