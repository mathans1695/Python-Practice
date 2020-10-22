counting = True
first = int(input())
second = int(input())

i = 1
while counting:
	if i % first == 0 and i % second == 0:
		print(i)
		break
	i += 1
