# Polymorphism 
# poly - means many 
# morphism - means forms 

class Animal:
    def make_sound(self):
        print("The animal makes a sound")
    
class Dog(Animal):
    def make_sound(self):
        print("The dog barks")

class Car(Animal):
    def make_sound(self):
        print("The cat meows")


# Polymorphism in action 
animals = [Dog(), Car()]

for animal in animals:
    animal.make_sound()



class Shape:
    def area(self):
        print("Calculating area....")

class Square(Shape):
    def area(self):
        print("Area of a Square: L * L")

class Circle(Shape):
    pass


# polymorphism in action

shapes = [Circle(), Square()]

for shape in shapes:
    print(shape.area())