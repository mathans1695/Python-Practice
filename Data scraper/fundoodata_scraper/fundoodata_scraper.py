from requests_html import HTML, HTMLSession
import csv

with open('coimbatore_fundoodata_companies.txt', 'r') as file:
	links = file.read().split('\n')
	
csv_file = open('coimbatore_data.csv','w',newline = '')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Company', 'Industry', 'Company Type', 'Sector' ,'Contact', 'Pincode', 'Address', 'Website'])

for link in links:
	session = HTMLSession()
	r = session.get(link)
	print(r.ok)
	if r.ok != True:
		continue
	
	html = r.html
	try:
		company_name = html.find('.search-page-heading-red', first=True).text
	except Exception:
		company_name = ''
	try:
		data = html.find('.search-page-right-pannel', first=True)
	except Exception:
		pass
	try:
		p_and_li = data.find('.detail-line', first=True).text.split(' ')
	
		if len(p_and_li) == 4:
			phone_num = '{}, {}'.format(p_and_li[1], p_and_li[2])
			website = p_and_li[3]
		
		elif len(p_and_li) == 3:
			phone_num = p_and_li[1]
			website = p_and_li[2]
		
		else:
			phone_num = ''
			website = p_and_li[0]
	except Exception:
		phone_num = ''
		website = ''
	try:
		overview = data.find('.overview-box2')
		industry = overview[0].text.split('\n')[1]
		company_type = overview[1].text.split('\n')[1]
		sector = overview[2].text.split('\n')[1]
	except Exception:
		industry = ''
		company_type = ''
		sector = ''
	try:
		trial = data.find('div')[0].text.split('\n')
		address_part1 = trial[2].split('- ')
		
		address = '{}, {}'.format(address_part1[1], trial[3])
		
		pin_code1 = address.split(',')
		pincode = pin_code1[len(pin_code1)-1].lstrip()
	except Exception:
		address = ''
		pincode = ''
	
	try:
		csv_writer.writerow([company_name, industry, company_type, sector, phone_num, pincode, address, website])
	except Exception:
		pass

csv_file.close()
	