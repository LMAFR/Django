class Circle():

    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_radius):
        self.radius = new_radius

my_circle = Circle()
# Si no añadimos paréntesis al llamar el método, este nos devuelve su ubicación en la memoria
print(my_circle.area) 
print(my_circle.area()) 

my_circle.set_radius(100)
print(my_circle.area())