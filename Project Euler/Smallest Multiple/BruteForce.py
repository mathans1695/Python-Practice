i = 20
while i:
	count = 1
	for j in range(2, 21):
		if i % j == 0:
			count += 1
		else:
			break
			
	if count == 20:
		print(i)
		break
	
	i += 20
