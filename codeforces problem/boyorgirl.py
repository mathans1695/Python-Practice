s = list(input())
length = len(s)
i = 0
while i < length:
	j = i+1
	while j < length:
		if s[i] == s[j]:
			if j == length-1:
				s.pop(j)
				length -= 1
			else:
				k = j+1
				temp = j
				while k < length:
					s[temp] = s[k]
					k += 1
					temp += 1
				s.pop(len(s)-1)
				length -= 1
		j += 1
	print(s)
		
	i += 1
		
print(len(s))