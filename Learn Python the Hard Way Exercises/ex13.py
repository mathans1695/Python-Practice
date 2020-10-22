from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "I am using raw input:%r" % raw_input("Write something to print it")

from sys import argv

first, second = argv

print "\n", first
print "\n", second
