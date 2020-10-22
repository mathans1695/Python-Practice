name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74.0
weight = 180.0
eyes = 'Blue'
teeth = 'white'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %r centimeters tall." % (height * 2.54)
print "He's %f pounds heavy." % (weight * 0.453592)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes[2], hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %f I get %f." % (age, height, weight, age + (height * 2.54) + (weight * 0.453592))

