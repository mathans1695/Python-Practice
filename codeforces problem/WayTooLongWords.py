n = int(input())
result = []

for i in range(n):
	word = input()
	if len(word) <= 10:
		result.append(word)
	else:
		result.append(word[0] + '{}'.format(len(word[1:len(word)-1])) + word[len(word)-1])

for i in result:
	print(i)