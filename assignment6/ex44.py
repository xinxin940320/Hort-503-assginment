#44.1.1 Implicit iheritance
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

#44.1.2 override explicitly

class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):
    def override(self):
        print("CHILD override()")
dad = Parent()
son = Child()

dad.override()
son.override()

#44.1.3 Alter before or after
class Parent(object):
    def altered(self):
        print("PARENT altered()")
class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")
dad = Parent()
son = Child()

dad.altered()
son.altered()

#44.1.4 All three combined
class Parent(object):
    def override(self):
        print("PARENT override()")
    def implicit(self):
        print("PARENT implicit()")
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

#44.2.1 composition

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):
    def __init__(self):
        self.other = Other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")
son = Child()
