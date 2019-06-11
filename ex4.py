#revsion


print('''
("python core data types are 1- immutable 2- mutable")
("#Immutable is - number, - string, - tuple")
("#Mutable is - list, - dictionary - files")

("@ 1- Numbers")

('There are three distinct numeric types: integers, floating point numbers and complex numbers')
('1- integers is a number like' , 5 , type(5))
('2- floating is a floating point' , 5.5, type(5.5))
('3- Complex is numbers have a real and imaginary part (x+yj)', type(5+9j))
'4- The constructors int(), float(), and complex() can be used to produce numbers of a specific type')
''')

# creat some variables

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# we do some math

cars_not_driven = cars - drivers # minus
cars_driven = drivers # equal
carpool_capacity = cars_driven * space_in_a_car # asterisk or multiplication
average_passengers_per_car = passengers / cars_driven # Division


print ("There are", cars, "Cars available")

print("There are only", drivers, "drivers available.")

print("There will be", cars_not_driven, "empty cars today")

print("We can transport", carpool_capacity, "people today.")

print("We have", passengers, "to carpool today.")

print("We need to put about", average_passengers_per_car, "in each car")