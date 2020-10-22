from bs4 import BeautifulSoup
import requests

web_link = 'http://coreyms.com'
next_page = True
while next_page:
	source = requests.get(web_link).text
	
	soup = BeautifulSoup(source, 'lxml')
	
	articles = soup.find_all('article')
	
	for article in articles:
		headline = article.header.a.text
		print(headline)
		
		description = article.div.p.text
		print(description)
		
		try:
			link_id = article.div.span.iframe['src'].split('?')[0].split('/')[4]
			link = 'http://www.youtube.com/watch?v=' + link_id
		
		except Exception:
			link = None
		
		print(link)
		
		print()
	
	try:
		page_link = soup.find('li', class_='pagination-next')
		web_link = page_link.a['href']
		
	except Exception:
		next_page = False
