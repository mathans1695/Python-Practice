# finding the greatest file or folder inside a specified folder

import os

greatest = -1
for folders, subfolders, files in os.walk('c:\\python27\\project euler'):
	if folders == 'c:\python27\project euler':
		continue
		
	total = 0
	for file in files:
		temp = os.path.join(folders, file)
		total += os.stat(temp).st_size
		
	if total > greatest:
		greatest = total
		greatestFol = folders
		
print(os.path.basename(greatestFol), greatest)