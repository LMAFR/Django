# INHERITANCE EXAMPLE

class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def eat(self):
        print("ANIMAL EATING")
    
    def sleep(self):
        print("ANIMAL SLEEPING")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")
    
    def bark(self):
        print("WOOF")

mydog = Dog()

mydog
mydog.eat()
mydog.sleep()
mydog.bark()