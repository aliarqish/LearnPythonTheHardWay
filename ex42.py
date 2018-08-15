## Animal is- a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## class Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has a __init__ that takes self and name parameters
        self.name = name

## class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has a __init__ that takes self and name parameters
        self.name = name

## class Person is-a object
class Person(object):

    def __init__(self, name):
        ## class Person has a __init__ that takes self and name parameters
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary attribute
        self.salary = salary

## class Fish is-a object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class Salmon is-a Fish
class Halibut(Fish):
    pass


## Set rover to an instance of Class Dog, which has-a attribute of name set to Rover.  Class Dog was called with params self and Rover.
rover = Dog("Rover")

## Set set to an instance of Class Cat and has-a attribute name set to Sat. Class Cat was called with params self and Sat.
sat = Cat("Sat")

## set mary to an instance of Person and has-a attribute name set to Mary
mary = Person("Mary")

## from mary get the pet attribute and set it to sat
mary.pet = sat

## frank is-a Employee instance has-a attribute name of Frank and attribute salary of 120000
frank = Employee("Frank", 120000)

## pet attribute of frank is-a rover
frank.pet = rover

## flipper is-a Fish instance
flipper = Fish()

## crouse is-a Salmon instance
crouse = Salmon()

## harry is Halibut instance
harry = Halibut()
