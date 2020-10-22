import sys
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def function(Male, Female):
	print "You gave %d points" % Male
	print "You gave %d points" % Female

print "What do you think about Male(out of 100): "
Male = int(raw_input())
print "What do you think about Female(out of 100): "
Female = int(raw_input())

function(Male, Female)
function(33, 67)
function(int(raw_input()), int(raw_input()))
function(int(sys.argv[1]), int(sys.argv[2]))
function(Male = 22, Female = 22)
function(int('11'), int('23'))