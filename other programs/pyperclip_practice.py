import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
	
	url = 'https://www.google.com/maps/place' + '/' + address
	
else:
	address = pyperclip.paste()
	
	url = 'https://www.google.com/maps/place/' + address
	
webbrowser.open(url)

