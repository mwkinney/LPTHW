## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a name that is set to name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self,name):
        ## cat has-a name that is set to name 
        self.name = name

## class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name that is set to name
        self.name = name

## Class person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name that is set to name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
        ## what is this strange magic?  
        super(Employee, self.__init__(name)
        ## Employee has-a salary set to salary
        self.salary = salary

## Fish is-a object 
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

# ??
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## frank is-a employee
frank = Employee("Frank", 120000)

## frank has-a pet named rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
