#This will import an argument variables from the sys(command prompt), argument variable is what you entered on command prompt, example: python ex15.py, in that ex15.py is argument variable. import is a feature or you can call that as modules too, python has more modules, you have to mention which modules you are going to use, here we are using argv modules, which gets input from user through terminal
from sys import argv

#What entered in command prompt will got assigned to the left variables equally
script, filename = argv

#the below line will open the file you have mentioned in the first stage of command prompt. That file will got assigned to the variable txt. But that txt will not have the content of it, txt variable just holds the file. In order to read the file, you have to use some other functions to do that.
txt = open(filename)

print "Here's your file %r:" % filename
#As I have already said, txt variable will have the file. But in order to access or read or write, you have to access the file use dot after the variable, followed by the functions you want to perform.
print txt.read()

print "Type the filename again:"
txt_again = open(raw_input('> '))

print "Here's your file: ", txt_again.write(stuff)

txt.close()
