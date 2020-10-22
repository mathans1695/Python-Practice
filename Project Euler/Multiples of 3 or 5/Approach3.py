R = 1000
# n3 will give number of multiple of 3 below R
n3 = (R-1) // 3

# n5 will give number of multiple of 5 below R
n5 = (R-1) // 5

# n15 will give number of multiple of 15 below R
n15 = (R-1) // 15

# s3 will give sum of multiple of 3 below R
s3 = 3*(n3*(n3+1)/2)

# s5 will give sum of multiple of 5 below R
s5 = 5*(n5*(n5+1)/2)

# s15 will give sum of multiple of 15 below R
s15 = 15*(n15*(n15+1)/2)

# result will give sum of multiple of 3 or 5 below R
result = (s3 - s15) + s5
print(result)