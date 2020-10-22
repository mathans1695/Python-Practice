import xlrd
import re

loc = 'data.xlsx'

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
count = 0

file = open('file.txt', 'w')

nameRE = re.compile(r'''
			\bshri\.*\b |
			\bmr\.*\b |
			\bsmt\.*\b
		''', re.VERBOSE | re.IGNORECASE)

def nameData(data):
	file.write(data)
	file.write('\n')

for i in range(sheet.nrows):
	curRowData = sheet.cell_value(i, 0)
	nameSearch = nameRE.search(curRowData)
	
	if(nameSearch):
		count += 1
		nameData(str(i+1))
		
print(count)
	