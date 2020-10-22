file = open("data.txt")
list = file.readlines()
arr2D = []
for i in list:
	arr2D.append(i.split())
	
for i in range(0, len(arr2D)):
	for j in range(0, len(arr2D[0])):
		arr2D[i][j] = int(arr2D[i][j])
new = open("new.txt", 'w')
greatest = 0
for i in range(0, len(arr2D)):
	for j in range(0, len(arr2D[0])):
		try:
			product = arr2D[i][j] * arr2D[i][j+1] * arr2D[i][j+2] * arr2D[i][j+3]
			new.write("{} {} {} {} = {}".format(arr2D[i][j], arr2D[i][j+1], arr2D[i][j+2], arr2D[i][j+3], product))
			new.write('\n')
			
			if product > greatest:
				greatest = product
				new.write("\n")
				new.write("{}".format(greatest))
				new.write("\n")
				
		except Exception:
			pass
			
		try:
			product = arr2D[i][j] * arr2D[i+1][j] * arr2D[i+2][j] * arr2D[i+3][j]
			new.write("{} {} {} {} = {}".format(arr2D[i][j], arr2D[i+1][j], arr2D[i+2][j], arr2D[i+3][j], product))
			new.write('\n')
			
			if product > greatest:
				greatest = product
				new.write("\n")
				new.write("{}".format(greatest))
				new.write("\n")
				
		except Exception:
			pass
			
		try:
			if (i - 1 < 0) or (i - 2 < 0) or (i - 3 < 0):
				pass
			else:
				product = arr2D[i][j] * arr2D[i-1][j] * arr2D[i-2][j] * arr2D[i-3][j]
				new.write("{} {} {} {} = {}".format(arr2D[i][j], arr2D[i-1][j], arr2D[i-2][j], arr2D[i-3][j], product))
				new.write('\n')
			
			if product > greatest:
				greatest = product
				new.write("\n")
				new.write("{}".format(greatest))
				new.write("\n")
				
		except Exception:
			pass
			
		try:
			if (j - 1 < 0) or (j - 2 < 0) or (j - 3 < 0):
				pass
			else:
				product = arr2D[i][j] * arr2D[i][j-1] * arr2D[i][j-2] * arr2D[i][j-3]
				new.write("{} {} {} {} = {}".format(arr2D[i][j], arr2D[i][j-1], arr2D[i][j-2], arr2D[i][j-3], product))
				new.write('\n')
			
			if product > greatest:
				greatest = product
				new.write("\n")
				new.write("{}".format(greatest))
				new.write("\n")
				
		except Exception:
			pass
			
		try:
			product = arr2D[i][j] * arr2D[i+1][j+1] * arr2D[i+2][j+2] * arr2D[i+3][j+3]
			new.write("{} {} {} {} = {}".format(arr2D[i][j], arr2D[i+1][j+1], arr2D[i+2][j+2], arr2D[i+3][j+3], product))
			new.write('\n')
			
			if product > greatest:
				greatest = product
				new.write("\n")
				new.write("{}".format(greatest))
				new.write("\n")
				
		except Exception:
			pass
			
		try:
			product = arr2D[i][j] * arr2D[i-1][j-1] * arr2D[i-2][j-2] * arr2D[i-3][j-3]
			new.write("{} {} {} {} = {}".format(arr2D[i][j], arr2D[i-1][j-1], arr2D[i-2][j-2], arr2D[i-3][j-3], product))
			new.write('\n')
			
			if product > greatest:
				greatest = product
				new.write("\n")
				new.write("{}".format(greatest))
				new.write("\n")
				
		except Exception:
			pass
			
		try:
			product = arr2D[i][j] * arr2D[i+1][j-1] * arr2D[i+2][j-2] * arr2D[i+3][j-3]
			new.write("{} {} {} {} = {}".format(arr2D[i][j], arr2D[i+1][j-1], arr2D[i+2][j-2], arr2D[i+3][j-3], product))
			new.write('\n')
			
			if product > greatest:
				greatest = product
				new.write("\n")
				new.write("{}".format(greatest))
				new.write("\n")
				
		except Exception:
			pass
		
		try:
			product = arr2D[i][j] * arr2D[i-1][j+1] * arr2D[i-2][j+2] * arr2D[i-3][j+3]
			new.write("{} {} {} {} = {}".format(arr2D[i][j], arr2D[i-1][j+1], arr2D[i-2][j+2], arr2D[i-3][j+3], product))
			new.write('\n')
			
			if product > greatest:
				greatest = product
				new.write("\n")
				new.write("{}".format(greatest))
				new.write("\n")
				
		except Exception:
			pass
		
print(greatest)