
num = (10, 12, 4, 7, 8, 9)

print(sorted(num))


a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a)

print(x)

y = sorted(a, reverse=True)
print(y)


# To sort a list by length, we can use the built-in len function.

names = ("Jenifer", "Sally", "Jane")
x = sorted(names, key=len)
print(x)



# Sort by a self made function for the key parameter.

# Sort the list by the number closest to 10:


def myfunc(n):
    return abs(10-n)

z = (4, 6, 3, 5, 7, 9, -8)
x = sorted(z, key=myfunc)
print(x)


# A lambda function can take any number of arguments, but can only have one expression.


# lambda arguments : expression

add10 = lambda x: x + 10

# add10 - function name
# lambda - keyword for defining function
# x - is the argument follow by the expression x + 10

print(add10(10))


z = (4, 6, 3, 5, 7, 9, -8)
x = sorted(z, key=lambda x: 10 - x)
print(x)


mult = lambda x,y: x * y

print(mult(2,7))


points_2D = [(1,2), (15, 1), (5, -1), (10, 4)]
points_2D_sorted = sorted(points_2D, key = lambda x: x[0] + x[1])


print(points_2D_sorted)


# map

some_list = [1, 2, 3, 4, 5, 6, 7]

multiply_by_2 = map(lambda x: x * 2 ,some_list)

print(list(multiply_by_2))