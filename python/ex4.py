#variable for number of cars
cars = 100
#variable for car's capacity(float)
space_in_a_car = 4.0
#number of drivers(integer)
drivers = 30
#number of passangers(integer)
passengers = 90
#number of empty cars(integer)
cars_not_driven = cars - drivers
#number of cars with drivers(integer)
cars_driven = drivers
#all capacity(float)
carpool_capacity = cars_driven * space_in_a_car
# (integer)
average_passengers_per_car = passengers / cars_driven

#output all variables
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."