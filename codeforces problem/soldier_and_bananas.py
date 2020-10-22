k, n, w = [int(x) for x in input().split(' ')]

borrow = n - (k * (w*(w+1))/2)

if borrow < 0:
	print(-1 * round(borrow))