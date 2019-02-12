## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## name is-a name
        self.name = name
## cat is-a animal
class Cat(Animal):
    def __init__(self, name):
        ## name is-a name
        self.name = name
## person is-a object
class Person(object):
    def __init__(self, name):
        ## name is-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None 28
## employee is-a person
class Employee(Person):

   def __init__(self, name, salary):
## employee has-a name
       super(Employee, self).__init__(name)
       ## salary is-a salary
       self.salary = salary



## fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

 ## halibut is-a fish
class Halibut(Fish):
    pass


 ## rover is-a Dog
 rover = Dog("Rover")
 ## Satan is-a cat
 satan = Cat("Satan")


 ## mary is-a person
 mary = Person("Mary")

 ## mary has-a pet of name as satan
 mary.pet = satan

 ## frank is-a employee has-a 120000-dollars salary
 frank = Employee("Frank", 120000)

 ## frank has-a pet named rover
 frank.pet = rover

 ## flipper has-a fish
 flipper = Fish()

 ## crouse has-a fish
 crouse = Salmon()

 ## harry has-a halibut
 harry = Halibut()
