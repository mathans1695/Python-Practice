import os, re

print('Enter the text you want to search:', end = ' ')
regex = input()
search = re.compile(r'{}'.format(regex))

for i in os.listdir():
	if os.path.splitext(i)[1] == '.txt':
		file = open(i)
		text = file.read()
		matches = search.finditer(text)
		for j in matches:
			print(i, j.span(), j.group())
		file.close()
	
