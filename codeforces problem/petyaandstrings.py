first, second = input().lower(), input().lower()

if first < second:
	print(-1)
elif second < first:
	print(1)
else:
	print(0)