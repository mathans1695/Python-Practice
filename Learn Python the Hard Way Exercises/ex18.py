def print_two1(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r args[1]: %r" % (arg1, arg2, args[1])

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got nothin'."

print_two1("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()