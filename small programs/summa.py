import random
from array1 import Array2D

_blank = Array2D(8, 8)

for i in range(random.randint(2,4)):
	ranI, ranJ = random.randint(0, 7), random.randint(0, 7)
	temp = random.choice([0, 1])
	
	list = [(ranI - 1, ranJ), (ranI + 1, ranJ), \
			(ranI, ranJ - 1), (ranI, ranJ + 1)]
	
	if temp == 0:
		for i in list:
			try:
				_blank[i[0], i[1]]
			except AssertionError:
				list.remove((i[0], i[1]))
		
		tuple = random.choice(list)
		for i in range(8):
			for j in range(8):
				if _blank[i, j] == '.':
					if _blank[tuple[0], tuple[1]] == '.':
						_blank[ranI, ranJ] = 0
						_blank[tuple[0], tuple[1]] = 1
			
	else:
		for i in list:
			try:
				_blank[i[0], i[1]]
			except AssertionError:
				list.remove((i[0], i[1]))
				
		tuple = random.choice(list)
		for i in range(8):
			for j in range(8):
				if _blank[i, j] == '.':
					if _blank[tuple[0], tuple[1]] == '.':
						_blank[ranI, ranJ] = 1
						_blank[tuple[0], tuple[1]] = 0


for i in range(8):
	for j in range(8):
		print(_blank[i, j], end = ' ')
	print()

