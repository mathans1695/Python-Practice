import re, os, shutil

regex = re.compile(r'0')

for file in os.listdir():
	changed = regex.sub(r'', file)
	os.rename(file, changed)
		
