arr = []
a = 6
b = 6

for i in range(2, a):
	arr.append(2**i)
	
for i in range(3, a):
	for j in range(2, b):
		val = i**j
		leng = len(arr)
		ind = leng // 2
		
		while leng > 2:
			if val > arr[ind]:
				leng = len(arr[ind+1 : leng])
				ind = (ind + 1) + leng // 2
				
			elif val < arr[ind]:
				leng = len(arr[0 : ind])
				ind = leng // 2
				
			else:
				pass
		
		if val > arr[ind//2]:
			arr.insert(ind//2, val)
		elif val < arr[ind//2]:
			arr.insert((ind//2)-1, val)
		else:
			pass
		
for i in arr:
	print(i)