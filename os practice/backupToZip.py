import os, zipfile, re

def backToZip(folder):
	folder = os.path.abspath(folder)
	
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number += 1
		
	backupZip = zipfile.ZipFile(zipFilename, 'w')
	for folders, subfolders, files in os.walk(folder):
		backupZip.write(folders, compress_type=zipfile.ZIP_DEFLATED)
		for i in files:
			newBase = os.path.basename(folder) + '_'
			if i.startswith(newBase) and i.endswith('.zip'):
				continue
			
			regex = re.compile(r'(?!.txt)$')
			match = regex.search(i)
			if match:
				backupZip.write(os.path.join(folders, i), compress_type=zipfile.ZIP_DEFLATED)
		
backToZip('.')