import xlrd
import re
import csv

loc = 'data.xlsx'

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

count = 0

nameRE = re.compile(r'''
			\bshri\.*\b |
			\bmr\.*\b |
			\bsmt\.*\b |
			\bms\.*\b |
			\bmrs\.*\b |
			\bsri\.*\b |
			\bdr\.*\b 
		''', re.VERBOSE | re.IGNORECASE)

def getCompany(data):
	return data
	
def getName(data):
	matches = nameRE.finditer(data)
	span = []
	moreThanOne = []
	final = ''
	
	for match in matches:
		span.append(match.span())
	
	if(len(span) > 1):
		for i in range(len(span)):
			if(len(span)-1 == i):
				name = data[span[i][1]:].strip('.').strip().strip(',').strip()
				moreThanOne.append(name)
			else:
				name = data[span[i][1]: span[i+1][0]].strip('.').strip().strip(',').strip()
				moreThanOne.append(name)
		final = moreThanOne[0]
	elif(len(span) == 1):
		final = data[span[0][1]:].strip('.').strip().strip(',').strip()
	else:
		final = data
		
	tempRE1 = re.compile(r'\s?-\s?')
	tempRE2 = re.compile(r'\s?,\s?')
	
	match1 = tempRE1.search(final)
	match2 = tempRE2.search(final)
	if(match1 != None):
		return final[0:match1.span()[0]]
	elif(match2 != None):
		return final[0:match2.span()[0]]
	else:
		if(final == ''):
			return 'Sir/Madam'
		else:
			return final
		
def getAddress(data):
	address = re.compile(r'Address:\s(.*)')
	mAddress = address.match(data)
	
	if(mAddress != None):
		adr = mAddress.group(1)
		splitted = adr.split(',')
		final = splitted[len(splitted)-1].strip().split(' ')
		
		str = ''.join(final)
		
		pincode = re.compile(r'\d{6}')
		listPincode = pincode.findall(str)
		if(listPincode):
			finalPincode = listPincode[0]
		else:
			finalPincode = ''
			
		return (final[0], finalPincode)
			
def getNumber(data):
	contactRE = re.compile(r'Contact Number:\s?(.*)')
	mContact = contactRE.match(data)
	phone = ''
	
	if(mContact != None):
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
		
		if(con != ''):
			if(temp.search(con)):
				contactTemp = temp.search(con)
				temp1 = contactTemp.span()[0]
				if(temp1 > 3):
					phone = con[0:temp1]
			else:
				phone = con
			
			process = re.sub(phoneRE, '', phone).strip(':').strip()
			process1 = re.sub(r'\s*-\s*', '', process)
			process2 = re.sub(r'\s*', '', process1)
			process3 = re.sub(r'/', ',', process2)
			
			return process3.split(',')[0]
			
		else:
			return ''
	
def getEmail(data):
	emailRE = re.compile(r'Email:\s?(.*)')
	mEmail = emailRE.match(data)
	
	if(mEmail):
		process1 = mEmail.group(1)
		process2 = re.sub(r';', ',', process1)
		return process2.split(',')[0]
	
	
csv_file = open('sample.csv', 'w', newline='')
fieldnames = ['company', 'name', 'city', 'pincode', 'number', 'email']
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
writer.writeheader()

def writeRow(company, name, address, number, email):
	global csv_file;
	try:
		writer.writerow({
			'company': company,
			'name': name,
			'city': address[0],
			'pincode': address[1],
			'number': number,
			'email': email
		})
	except:
		pass
	

for i in range(0, sheet.nrows, 5):
	company = getCompany(sheet.cell_value(i, 0))
	name = getName(sheet.cell_value(i+1, 0))
	address = getAddress(sheet.cell_value(i+2, 0))
	number = getNumber(sheet.cell_value(i+3, 0))
	email = getEmail(sheet.cell_value(i+4, 0))
	
	writeRow(company, name, address, number, email);