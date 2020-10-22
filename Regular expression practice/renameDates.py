import re, os, shutil

regex = re.compile(r'''^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)?\d\d)
(.*?)$
''', re.VERBOSE)

for text in os.listdir():
	result = regex.sub(r'\1\4-\2-\6\8', text)
	shutil.move(text, result)