import re, os, shutil

regex = re.compile(r'^practice_(.*?)([.])(.*?)$')

for file in os.listdir():
	result = regex.sub(r'\1\2\3', file)
	shutil.move(file, result)