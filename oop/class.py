# class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # class method
    def display_info(self):
        print(f"This is a {self.brand} {self.model}.")


# Object
car = Car("Benz", "GLE 350")
car.display_info()


car = Car("Tesla", "Model 3")
car.display_info()



class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

dog1 = Dog("Buddy", "Goldern Retriever")
dog2 = Dog("Max", "Bulldog")


dog1.bark()
dog2.bark()

