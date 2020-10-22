#A new variable cars has been created and assigned a value of 100

cars = 100
#Another variable space in a car has been created and assigned a value of 4.0, which is floating point number which means decimal number. 32 bit computer can store number upto 23 digits precisions and another digit for storing positive or negative sign

space_in_a_car = 4.0 #Floating point number is not needed here, because car space will always be a whole number
drivers = 30.0

passengers = 91
#Here, subtration function used, so computer activates minus function, after taking values from the two variable, calculation will be performed and the final value will get stored in newly created variable which is cars_not_driven

cars_not_driven = cars - drivers #As you may see all the variables has underscore, it is alternative to space, not literally. You can use some other symbols too to separate words. I think in python programming is not used. I tried using other symbols rather than underscore, but while executing the program, it is showing error. Therefore, underscore used for alternative to space

#drivers variable type and values got copied to cars_driven variable, which is newly created one
cars_driven = drivers

#Here multiplication was taking place, since space in car variable is floating point number, the result will also be a floating point number
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are %s only", drivers, "drivers available"
print "Hey %s there." % "you"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"