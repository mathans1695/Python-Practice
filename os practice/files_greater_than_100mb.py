import os

limit = 100
for folders, subfolders, files in os.walk('F:\\'):
	for file in files:
		temp = os.path.getsize(os.path.join(folders, file))
		condition = temp / (1024 * 1024)
		
		if condition >= limit:
			print(os.path.join(folders, file))