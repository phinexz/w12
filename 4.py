#tot cars
cars = 100
#space in a single car
space_in_a_car = 4
#tot drivers
drivers = 30
#tot passemgers
passengers = 90
#cars not driven
cars_not_driven = cars - drivers
#cars driven is total no. of drivers
cars_driven = drivers
#total capacity of driving cars
carpool_capacity = cars_driven * space_in_a_car
#rate of passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
