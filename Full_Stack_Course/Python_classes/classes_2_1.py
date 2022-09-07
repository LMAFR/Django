class Dog():
    
    # Class object attribute
    species = "mammal"
# All dogs are mammals, if you want to define a variable constant for all the instances of a class, we do it like in the previous line.


    # A method looks like a function inside a class (init is a constructor and self is a required variable):
    def __init__(self, name, breed = "yorkshire"):
        # variables to the right of self are attributes of the class, you can give them a default value by adding "= value" in the previous line brackets
        self.breed = breed
        self.name = name

mydog = Dog(breed = "Lab", name = "Tom")
otherdog = Dog(breed = "Huskie", name = "Lana")
moredogs = Dog(name = "Man")

print(mydog.breed)
print(otherdog.name)
print(mydog.species)
print(otherdog.species)
print(moredogs.breed)