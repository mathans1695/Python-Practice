n, k = map(int, input().split(' '))
scores = list(map(int, input().split(' ')))

qual = scores[k-1]
if qual == 0:
	count = 0
	for i in range(k-2, -1, -1):
		if scores[i] > 0:
			count = i + 1
			break
			
else:
	count = k
	for i in range(k, len(scores)):
		if scores[i] == qual:
			count += 1
		else:
			break
	
print(count)

