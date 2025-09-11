import math_operations as math_op
import platform

num1 = 10
num2 = 5


print("Addition", math_op.add(num1, num2))
print("Subtraction", math_op.subtract(num1, num2))
print("Multiplication", math_op.multiply(num1, num2))
print("Division", math_op.divide(num1, num2))



x = platform.system()
print(x)


# List all the defined names belonging to the platform module:

dir = dir(platform)
print(dir)
