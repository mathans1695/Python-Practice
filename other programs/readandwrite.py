from sys import argv
from os.path import exists

script, input, output = argv

print "File %s will be copied to %s" % (input, output)

open(output, 'w').write("%s\n " % open(input).read())