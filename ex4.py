cars = 100
spaces_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carapool_capacity = cars_driven*spaces_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carapool_capacity, "people today")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
"in each car.")