# str, len and del initial methods

from enum import auto


class Book():

    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages

    # The print function looks for the string representation of the class when it calls an instance. Such representation is defined with the str special method
    def __str__(self):
        return "This book was written by {}, its name is {} and has {} pages.".format(self.author, self.title, self.pages)
    # If we do not define the string representation, print will return the memory location of the class definition

    # In the same way, the len function looks for the definition given by the len special method in the class definition:
    def __len__(self):
        return self.pages

    # Finally, the del special method can be used to return something when an instance is deleted using the built-in function "del"
    def __del__(self):
        print("A book has been destroyed!")


mybook = Book(author = "Peter", title = "Calamities", pages = 200)

print(mybook)
print(len(mybook))

del mybook
