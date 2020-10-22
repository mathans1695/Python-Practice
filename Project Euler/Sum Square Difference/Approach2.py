n = 100
sum, sum1 = 0, 0

sum = (n * ((n + 1) / 2)) ** 2
sum1 = n * (((n + 1) * (2 * n + 1)) / 6)

print(abs(sum - sum1))