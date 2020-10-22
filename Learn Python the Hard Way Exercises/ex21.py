def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
def simple_formula(a, b, c, d):
	print "SIMPLE FORMULA: "
	return a + b - c * d / 2
	
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(3, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight,divide(iq, 2))))

what1 = age + height - weight * iq / 2

print "That becomes: ", what, "Can you do it by hand?"

print "Normal formula: ", what1

print "Simple formula: ", simple_formula(age, height, weight, iq)