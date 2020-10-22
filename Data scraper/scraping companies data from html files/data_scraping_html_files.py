from bs4 import BeautifulSoup
import os
import codecs
import csv

def parseHTML(path):
	f = codecs.open(path, 'r', encoding='utf-8')
	text = f.read()
	document = BeautifulSoup(text, 'html.parser')
	data = document.find_all('font')
	li = []
	dic = {
		'industry': '',
		'company': '',
		'address': '',
		'phone': '',
		'fax': '', 
		'email': '',
		'other_emails': '',
		'website': '',
		'contact': '',
		'other_contact': '',
		'business_details': ''
	}
	
	for i in range(0, len(data), 1):
		newData = data[i].string
		
		dic['industry'] = data[0].string
		
		if(newData == '*'):
			try:
				dic_copy = dic.copy()
				dic = {
					'industry': '',
					'company': '',
					'address': '',
					'phone': '',
					'fax': '', 
					'email': '',
					'other_emails': '',
					'website': '',
					'contact': '',
					'other_contact': '',
					'business_details': ''
				}
				
				li.append(dic_copy)
				dic['company'] = data[i+1].string
			except:
				pass

		elif(newData == '_____________________________________________________________________________'):
			dic['company'] = data[i+1].string
			
		elif(newData == 'Address'):
			new = ''
			for j in range(i+1, len(data), 1):
				temp = data[j].string
				if(temp == 'Phone:' or temp == 'Fax:' or temp == 'Email:' or temp == 'Website:' or temp == 'Contact:' or temp == 'Business Details:'):
					break
				new += temp
			city = new.split(',')
			try:
				dic['address'] = city[len(city) - 1].strip().split()[0]
			except: 
				dic['address'] = ''
			
		elif(newData == 'Phone:'):
			new = ''
			for j in range(i+1, len(data), 1):
				temp = data[j].string
				if(temp == 'Fax:' or temp == 'Email:' or temp == 'Website:' or temp == 'Contact:' or temp == 'Business Details:'):
					break
				new += temp
			dic['phone'] = new
			
		elif(newData == 'Fax:'):
			new = ''
			for j in range(i+1, len(data), 1):
				temp = data[j].string
				if(temp == 'Email:' or temp == 'Website:' or temp == 'Contact:' or temp == 'Business Details:'):
					break
				new += temp
			dic['fax'] = new
			
		elif(newData == 'Email:'):
			new = ''
			for j in range(i+1, len(data), 1):
				temp = data[j].string
				if(temp == 'Website:' or temp == 'Contact:' or temp == 'Business Details:'):
					break
				new += temp
			splited = new.split(',')
			
			try:
				if(len(splited) > 1):
					dic['email'] = splited[0]
					other_emails = ''
					for email in splited[1:]:
						other_emails += email.strip() + ', '
					other_emails = other_emails.strip(', ')
					dic['other_emails'] = other_emails
				else:
					dic['email'] = splited[0]
					dic['other_emails'] = ''
			except:
				dic['email'] = ''
				dic['other_email'] = ''
		
		elif(newData == 'Website:'):
			new = ''
			for j in range(i+1, len(data), 1):
				temp = data[j].string
				if(temp == 'Contact:' or temp == 'Business Details:'):
					break
				new += temp
			dic['website'] = new
			
		elif(newData == 'Contact:'):
			new = ''
			for j in range(i+1, len(data), 1):
				temp = data[j].string
				if(temp == 'Business Details:'):
					break
				new += temp
				
			splited = new.split(',')
			
			try:
				if(len(splited) > 1):
					dic['contact'] = splited[0]
					other_contact = ''
					for contact in splited[1:]:
						other_contact += contact.strip() + ', '
					other_contact = other_contact.strip(', ')
					dic['other_contact'] = other_contact
				else:
					dic['contact'] = splited[0]
					dic['other_contact'] = ''
			except:
				dic['contact'] = ''
				dic['other_contact'] = ''
			
		elif(newData == 'Business Details:'):
			new = ''
			for j in range(i+1, len(data), 1):
				temp = data[j].string
				if(temp == '*'):
					break
				new += temp
			dic['business_details'] = new
			
	return li
		
with open('sample.csv', mode='w', newline='') as csv_file:
	fieldnames = ['industry', 'company', 'address', 'phone', 'fax', 'email', 'other_emails', 'website', 'contact', 'other_contact', 'business_details']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writeheader()
	
	count = 0
	for (root, dirs, files) in os.walk('C:/Users/suresh/Desktop/Dev/Python/companies data in html files/10/'):
		for file in files:
			try:
				data = parseHTML(root + '/' + file)
				for indivData in data:
					writer.writerow(indivData)
			except:
				print(file)

#data = parseHTML('Agro Products & CommoditiesPage2.html')
		
#with open('sample.csv', mode='w', newline='') as csv_file:
#	fieldnames = ['industry', 'company', 'address', 'phone', 'fax', 'email', 'other_emails', 'website', 'contact', 'other_contact', 'business_details']
	
#	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#	writer.writeheader()
	
#	for indivData in data:
#		writer.writerow(indivData)

