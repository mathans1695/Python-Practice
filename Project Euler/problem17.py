arr = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'onehundred', 'onethousand']

new = ['']
for i in range(1, 21):
	new.append(arr[i])

for i in range(21, 1001):
	if i > 20 and i < 30:
		new.append(arr[20] + arr[i % 10])
		
	elif i >= 30 and i < 40:
		new.append(arr[21] + arr[i % 10])
		
	elif i >= 40 and i < 50:
		new.append(arr[22] + arr[i % 10])
	
	elif i >= 50 and i < 60:
		new.append(arr[23] + arr[i % 10])
		
	elif i >= 60 and i < 70:
		new.append(arr[24] + arr[i % 10])
		
	elif i >= 70 and i < 80:
		new.append(arr[25] + arr[i % 10])
		
	elif i >= 80 and i < 90:
		new.append(arr[26] + arr[i % 10])
		
	elif i >= 90 and i < 100:
		new.append(arr[27] + arr[i % 10])
		
	elif i == 100:
		new.append(arr[28])
		
	elif i > 100 and i < 200:
		new.append(arr[28] + 'and' + new[i % 100])
		
	elif i == 200:
		new.append('twohundred')
		
	elif i > 200 and i < 300:
		new.append('twohundred' + 'and' + new[i % 100])
	
	elif i == 300:
		new.append('threehundred')
		
	elif i > 300 and i < 400:
		new.append('threehundred' + 'and' + new[i % 100])
		
	elif i == 400:
		new.append('fourhundred')
		
	elif i > 400 and i < 500:
		new.append('fourhundred' + 'and' + new[i % 100])
		
	elif i == 500:
		new.append('fivehundred')
		
	elif i > 500 and i < 600:
		new.append('fivehundred' + 'and' + new[i % 100])
		
	elif i == 600:
		new.append('sixhundred')
		
	elif i > 600 and i < 700:
		new.append('sixhundred' + 'and' + new[i % 100])
		
	elif i == 700:
		new.append('sevenhundred')
		
	elif i > 700 and i < 800:
		new.append('sevenhundred' + 'and' + new[i % 100])
		
	elif i == 800:
		new.append('eighthundred')
		
	elif i > 800 and i < 900:
		new.append('eighthundred' + 'and' + new[i % 100])
		
	elif i == 900:
		new.append('ninehundred')
		
	elif i > 900 and i < 1000:
		new.append('ninehundred' + 'and' + new[i % 100])
		
	else:
		new.append(arr[29])
	
sum = 0
for i in range(0, 1001):
	sum += len(new[i])
	
print(sum)