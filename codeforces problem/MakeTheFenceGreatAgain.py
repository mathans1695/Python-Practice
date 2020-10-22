result = []
for x in range(int(input())):
	n = int(input())
	boards = []
	for j in range(n):
		t1, t2 = list(map(int, input().split(' ')))
		boards.append(t1)
		boards.append(t2)
		
	cost = 0
	diff = None
	cop = boards.copy()
	z = 3
	happen = 0
	for i in range(0, len(boards)-z, 2):
		temp, temp1 = 0, 0
		if boards[i] == boards[i + 2]:
			if boards[i+1] >= boards[i+3]:
				temp += boards[i+3]
				boards[i+2] += 1
			
				try:	
					if boards[i+2] == boards[i+4]:
						if boards[i+3] >= boards[i+5]:
							temp += boards[i+5]
							boards[i+4] += 1
							
						else:
							temp += boards[i+3]
							boards[i+2] += 1
							
					if cop[i] == cop[i+2]:
						temp1 += cop[i+1]
						cop[i+1] += 1
						
					if temp > temp1:
						boards = cop.copy()
						cost += temp1
						happen = 1
					z += 3
						
				except IndexError:
					pass
					
				if happen == 0:
					cost += temp
					
			else:
				cost += boards[i+1]
				boards[i] += 1
				
	result.append(cost)
	
for i in result:
	print(i)

