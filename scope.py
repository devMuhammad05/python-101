# Scope 

# Local scope
# Global scope


# Local scope

def greet():
    message = "Hello World"
    print(message)

greet()

# can't access variable message here because it is local scope
# print(message)



# Global scope

greeting = "Hii"

def say_hii():
    print(greeting)

say_hii()

print(greeting + " from outside the function")