s = input()
if 97 <= ord(s[0]) <= 122:
	s = chr(ord(s[0]) - 32) + s[1:len(s)]
print(s)