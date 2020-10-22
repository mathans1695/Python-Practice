import sys
t = int(input())
result = []

for i in range(t):
	data = input().split(' ')
	n, m  = int(data[0]), int(data[1])
	if 1 <= n <= min((2**m - 1), 100):
		pass
	else:
		n = min((2**m - 1), 100)
	
	a = []
	
	for i in range(n):
		inp = input()
		a.append(inp)
	
	t = []
	for i in range(m):
		t.append('0')
	
	set = []
	set.append(t)
	
	condition = []
	for i in range(len(t)):
		if i == 0:
			condition.append('0')
		else:
			condition.append('1')
	
	i = 0
	temp = '0'
	while t != condition:
		temp = set[len(set)-1].copy()
		for j in range(len(temp)-1, i, -1):
			t = temp.copy()
			t[j] = '1'
			set.append(t)
		i += 1
	
	temp = []
	for i in range(len(set)):
		new = []
		for j in range(len(set[0])):
			new.append(set[i][j])
		temp.append(new)
		
	for i in temp:
		i[0] = '1'
		set.append(i)
		
	print(sys.getsizeof(set))
	
	sequence = []
	for i in set:
		new = ''
		for j in range(len(i)):
			new += i[j]
		sequence.append(new)
		
	set.clear()

	for i in a:
		temp = sequence.copy()
		mid = None
		while mid != 0:
			mid = len(temp) // 2
			if i < temp[mid]:
				temp = temp[0:mid]
			
			elif i > temp[mid]:
				temp = temp[mid+1:len(temp)]
			
			else:
				sequence.remove(i)
				break
	
	if len(sequence) % 2 != 0:
		result.append(sequence[len(sequence) // 2])
	else:
		m = len(sequence) // 2
		result.append(sequence[((m-1) + m)//2])
		
for i in result:
	print(i)
	