from sys import argv

script, filename = argv

open = open(filename, 'a')
print "File opened in write mode, typein whatever you want"

line4 = raw_input("Type what you want to add: (you can add one line: ")
line5 = raw_input("Type the next line: ")

print "That's enough, you have typed two lines, I'll include those lines in the file"

open.write("\n")
open.write(line4)
open.write("\n")
open.write(line5)

print "Lines added to the document"

open.close()