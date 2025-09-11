

# def factorial(n):
#     value = 1

#     if n == 0 or n == 1:
#         print(1)
#         return
    
#     for number in range(1, n+1):
#         if not number == 0:
#             value *= number
#         print(value)

# factorial(5)


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    

# number = factorial(5)
# print(number)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero not allowed"