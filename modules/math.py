# Built-in Math Functions
# The min() and max() functions can be used to find the lowest or highest value in an iterable:



# The Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions.

import math

print(math.sqrt(64))

# rounds up to the nearest whole number 
print(math.ceil(2.1))


# rounds down to the nearest whole number 
print(math.floor(2.7))


# The math.pi constant, returns the value of PI (3.14...):

c = math.pi
print(c)



# The min() and max() functions can be used to find the lowest or highest value in an iterable:

z = min(5, 10, 25)
print(z)

y = max(5, 10, 25)
print(y)

# The abs() function returns the absolute (positive) value of the specified number:
r = abs(-7.33)
print(r)



# The pow(x, y) function returns the value of x to the power of y (xy).
f = pow(4, 3)   # 4 * 4 * 4
print(f)