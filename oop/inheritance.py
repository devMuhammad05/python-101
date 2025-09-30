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