# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")


# Child class 
class Dog(Animal):
    def barks(self):
        print("Dog barks")


dog = Dog()
dog.sound()


class Parent:
    def display(Self):
        print("I am a Parent class")

class  Child(Parent):
    pass


child = Child()
child = child.display()



# multiple inheritance
class A:
    def method_a(self):
        print("I am method A")

class B:
    def method_b(self):
        print("I am method B")

class C(A, B):
    pass

obj = C()
obj.method_a()
obj.method_b()



# Multi level inheritance
class GradParent:
    def display(self):
        print("I am a Grand Parent class")

class Parent(GradParent):
    pass

class Child(Parent):
    pass

child = Child()
child.display()


class Animal:
    def __init__(self):
        print("Animal Created")

class Dog(Animal):
    def __init__(self):
        super().__init__()  #inherit the methods and properties from its parent.
        print("Dog Created")

dog = Dog()




class Vehicle:
    def fuel_type(self):
        print("Fuel type: Petrol/Diesel")

class ElectricCar(Vehicle):
    def fuel_type(self):
        print("Fuel type: Electric")
    

car = ElectricCar()
car.fuel_type()
