from sys import argv

script, input_file = argv

def print_all(f):
	print f.read(),
	print f.tell()
	
#The seek function will be move the cursor to the start of the file by calling the seek function with value 0 and if you put 1, instead of 0, the cursor will move to the next word, ie.) T will be removed from reading
def rewind(f):
	f.seek(0)
	f.tell()

#During first call, line_count value will be one and first line will be read by the system and EOL line will be applied
#During second call, line count value will be two and second line will be read by the system and the cursor will be moved to next line
#During third call, line count will be three and third line will be read by the system and the cursor will be moved to End of Line	
def print_a_line(line_count, f):
	print line_count, f.readline()

#file object will be assigned to current file	
current_file = open(input_file)

print "First let's print the whole file:\n"

#file object got transferred using function call
print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

#Current line value is 1 and it passes 1 value to line_count variable
current_line = 1
print_a_line(current_line, current_file)

#Current line value is 2 now and now it passes 2 to line count variable
current_line += 1
print_a_line(current_line, current_file)

#Current line value is 3 now and now it passes 3 to line count variable
current_line += 1
print_a_line(current_line, current_file)