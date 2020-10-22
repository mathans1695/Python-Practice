s = [int(x) for x in input().split('+')]

for i in range(len(s)):
	smallest = s[i]
	for j in range(i+1, len(s)):
		if s[j] < smallest:
			smallest = s[j]
			swap = s[i]
			s[i] = s[j]
			s[j] = swap
			
print('+'.join([str(x) for x in s]))