num = int(input())
stones = input()

remove = 0
for i in range(num - 1):
	if stones[i] == stones[i+1]:
		remove += 1

print(remove)