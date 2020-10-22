arr = []
r, c = 1001, 1001
for i in range(r):
	new = []
	for j in range(c):
		new.append(0)
	arr.append(new)
	
arr[r//2][c//2] = 1

row = r//2
col = c//2

arr[row][col+1] = arr[row][col] + 1
col += 1
temp_col = 1
temp_row = 0

for i in range(1001999):
	if temp_col == 1 and temp_row == 0:
		if col == len(arr[0]) - 1:
			arr[row+1][col] = arr[row][col] + 1
			row += 1
			temp_col = 0
			temp_row = 1
			
		else:		
			if arr[row+1][col] == 0 and arr[row][col+1] == 0:
				arr[row+1][col] = arr[row][col] + 1
				row += 1
				temp_col = 0
				temp_row = 1
					
			elif arr[row+1][col] != 0 and arr[row][col+1] == 0:
				arr[row][col+1] = arr[row][col] + 1
				col += 1
				temp_col = 1
				temp_row = 0
			
	elif temp_col == 0 and temp_row == 1:
		if row == len(arr) - 1:
			if arr[row][col-1] == 0:
				arr[row][col-1] = arr[row][col] + 1
				col -= 1
				temp_col = -1
				temp_row = 0
		else:
			if arr[row][col-1] == 0 and arr[row+1][col] == 0:
				arr[row][col-1] = arr[row][col] + 1
				col -= 1
				temp_col = -1
				temp_row = 0
		
			elif arr[row][col-1] != 0 and arr[row+1][col] == 0:
				arr[row+1][col] = arr[row][col] + 1
				row += 1
				temp_col = 0
				temp_row = 1
			
	elif temp_col == -1 and temp_row == 0:
		if col == 0:
			if arr[row-1][col] == 0:
				arr[row-1][col] = arr[row][col] + 1
				row -= 1
				temp_col = 0
				temp_row = -1
				
		else:
			if arr[row-1][col] == 0 and arr[row][col-1] == 0:
				arr[row-1][col] = arr[row][col] + 1
				row -= 1
				temp_col = 0
				temp_row = -1
			
			elif arr[row-1][col] != 0 and arr[row][col-1] == 0:
				arr[row][col-1] = arr[row][col] + 1
				col -= 1
				temp_col = -1
				temp_row = 0
			
	elif temp_col == 0 and temp_row == -1:
		if row == 0:
			if arr[row][col+1] == 0:
				arr[row][col+1] = arr[row][col] + 1
				col += 1
				temp_col = 1
				temp_row = 0
			
		else:
			if arr[row][col+1] == 0 and arr[row-1][col] == 0:
				arr[row][col+1] = arr[row][col] + 1
				col += 1
				temp_col = 1
				temp_row = 0
		
			elif arr[row][col+1] != 0 and arr[row-1][col] == 0:
				arr[row-1][col] = arr[row][col] + 1
				row -= 1
				temp_col = 0
				temp_row = -1			
			
row = 0
col = 0
sum = 0
for i in arr:
	print(i)

while row != len(arr) and col != len(arr[0]):
	sum += arr[row][col]
	row += 1
	col += 1
	
row = len(arr) - 1
col = 0
while row != -1 and col != len(arr[0]):
	sum += arr[row][col]
	row -= 1
	col += 1
	
sum -= 1
print(sum)