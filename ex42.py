
## animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    pass

## is-a a sub class
class Dog(Animal):
    def __init__(self, name):
        ## attributes
        self.name = name

## is-a a sub class
class Cat(Animal):
    def __init__(self, name):
        ## attributes
        self.name = name


## is-a a class
class Person(object):
    def __init__(self, name):
        ## attributes
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## is-a a sub class
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ## attributes
        self.salary = salary

## ??
class Fish(object):
    pass


class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

## rover is-a Dog

rover = Dog("Rover")

## is-a an object - instance of a class
satan = Cat("Satan")

## is-a an object - instance of a class
mary = Person("Mary")

## has-a
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## has-a
frank.pet = rover

## is-a an object - instance of a class
flipper = Fish()

## is-a an object - instance of a class
crouse = Salmon()

## is-a an object - instance of a class
harry = Halibut