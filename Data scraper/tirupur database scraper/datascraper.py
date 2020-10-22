import xlrd
import re

loc = 'data.xlsx'

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

address = re.compile(r'Address:\s(.*)')
contact = re.compile(r'Contact Number:\s(.*)')
count = 0
countCon = 0

file = open('file.txt', 'w');

for i in range(0, sheet.nrows):
	cur = sheet.cell_value(i, 0)
	mAddress = address.match(cur)
	mContact = contact.match(cur)
	print(mContact)
	
	if(mAddress != None):
		count += 1
		adr = mAddress.group(1)
		splitted = adr.split(',')
		final = splitted[len(splitted)-1].strip().split(' ')
		
		str = ''.join(final)
		
		pincode = re.compile(r'\d{6}')
		listPincode = pincode.findall(str)
	elif(mContact != None):
		phoneRE = re.compile(r'''
						Phone\s*: |
						Mob\s*: | 
						Tel\s*: | 
						Ph\s* | 
						Mobile\s*: | 
						Tele\s: |
						phone\s*: |
						mob\s*: |
						tel\s*: |
						ph\s*: |
						mobile\s*: |
						tele\s*: ''', re.VERBOSE)
						
		temp = re.compile('Fax')
		con = mContact.group(1)
		
		if(temp.search(con)):
			contactTemp = temp.search(con)
			countCon += 1
			temp1 = contactTemp.span()[0]
			if(temp1 > 3):
				phone = con[0:temp1]
		else:
			phone = con
			countCon += 1
		
		finalSearch = phoneRE.finditer(phone)
		
		print(list(finalSearch))

print(count, countCon)