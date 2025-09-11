# handling errors and exceptions 

# a = 5 + '10'  TypeError: unsupported operand type(s) for +: 'int' and 'str'

# print(5 / 0)  ZeroDivisionError: division by zero

try: 
    a = 5 / 1
    a = 5 + '10' 
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else: 
    print("Everything works fine")
finally: 
    print("final clean up....")




# Raise an exception
# The raise keyword is used to raise an exception.


x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")


x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")


