import os, shutil

os.mkdir('c:\\users\\suresh\\downloads\\newfolder')
lis = list()

for folders, subfolders, files in os.walk('c:\\users\\suresh\\downloads'):
	temp = os.path.abspath(folders)
	for file in files:
		if file.endswith('.pdf') or file.endswith('.jpg'):
			source = os.path.join(temp, file)
			destination = 'c:\\users\\suresh\\downloads\\newfolder'
			lis.append(file)
			try:
				shutil.copy(source, destination)
			except:
				pass
				
print(lis)