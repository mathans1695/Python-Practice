import os, re, shutil
	
regex = re.compile(r'(.*)(\d\d\d)$')
lis = []
ext = []
i = -1
base_path = 'c:\\users\\suresh\\desktop\\dev\\python\\os practice\\filling_gaps'

for file in os.listdir(base_path):
	text = os.path.splitext(file)[0]
	match = regex.search(text)
	
	if match:
		ext.append(os.path.splitext(file)[1])
		lis.append(match)
		i += 1
		
		try:
			if len(lis) > 1:
				if lis[i].group(2) == lis[i-1].group(2):
					lis.remove(lis[i])
					lis.remove(lis[i-1])
					ext.remove(ext[i])
					ext.remove(ext[i])
		except Exception:
			pass
print(lis)
j = int(lis[0].group(2)) + 1
for i in range(1, len(lis)):
	print(j)
	if int(lis[i].group(2)) != j:
		print(lis[i].group(2))
		add = os.path.join(base_path, '{}{}{}'.format(lis[i].group(1), j, ext[0]))
		j += 1
	
	j += 1
	