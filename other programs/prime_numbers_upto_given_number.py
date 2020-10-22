n = 100
list = []
for i in range(2, n):
	list.append(i)
	
for i in range(len(list)):
	for j in range(i + 1, len(list)):
		try:
			if list[j] % list[i] == 0:
				list.remove(list[j])
				print(list[j])
		except:
			pass
	if len(list) == 10000:
		break
			
print(list)