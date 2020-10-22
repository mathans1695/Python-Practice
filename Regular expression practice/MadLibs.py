import re

file = open('madlibstext.txt', 'r')
f_text = file.read()
	
temp = re.compile(r'(\bADJECTIVE\b)|(\bNOUN\b)|(\bVERB\b)|(\bADVERB\b)')
matches = temp.finditer(f_text)

new_line_re = re.compile(r'\n')
or_new_line = list(new_line_re.finditer(f_text))

copy = f_text
j = 0
for i in range(len(list(matches))):
	match = temp.search(copy)
	
	if match.group() == 'ADJECTIVE':
		print('Enter an ' + match.group().lower())
		
	else:
		print('Enter a ' + match.group().lower())
	
	inp = input()
	start = match.span()[0]
	end = match.span()[1]
	output = copy[0:start] + inp + copy[end:]
	
	copy = output
	
	new_line = list(new_line_re.finditer(copy))
	if j < len(or_new_line):
		if new_line[j].span()[0] > or_new_line[j].span()[0]:
			output = copy[0:new_line[j].span()[0]] + ' ' + copy[new_line[j].span()[1]:]
			copy = output
			output = copy[0:or_new_line[j].span()[0]] + '\n' + copy[or_new_line[j].span()[0]:]
			copy = output
			
			j += 1

file.close()
file = open('output.txt', 'w')
file.write(copy)
file.close()