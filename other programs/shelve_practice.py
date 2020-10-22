import sys, pyperclip, shelve

def saveText(name):
	file = shelve.open('clipboard')
	file[name] = pyperclip.paste()
	file.close()

def listKeys():
	file = shelve.open('clipboard')
	key = '\n'.join(list(file.keys()))
	pyperclip.copy(key)
	file.close()
	
def copyToClipboard(name):
	file = shelve.open('clipboard')
	
	if name in file.keys():
		pyperclip.copy(file[name])
		
	file.close()
	
def delete(name):
	file = shelve.open('clipboard')
	if name in file:
		del file[name]
	file.close()
	
def delete_all():
	file = shelve.open('clipboard')
	for name in file.keys():
		del file[name]
	file.close()
	

if len(sys.argv) != 1:
	if sys.argv[1] == 'save':
		saveText(sys.argv[2])
		
	elif sys.argv[1] == 'list':
		listKeys()
		
	elif sys.argv[1] == 'delete':
		delete(sys.argv[2])
		try:
			if sys.argv[2] == 'all':
				delete_all()
		except Exception:
			pass
		
	else:
		copyToClipboard(sys.argv[1])