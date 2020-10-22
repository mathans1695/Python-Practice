from sys import argv

script, user_name, gender = argv
prompt = '> '

print " Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
print "You're %s, so you will have a big penis, that will be useful to please a girl, is that right?" % gender

reply = raw_input(prompt)
print "You said %s that's good" % reply

likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)