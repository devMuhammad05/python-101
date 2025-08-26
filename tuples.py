
# From Python's perspective, tuples are defined as objects with the data type 'tuple':

mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(len(mytuple))
print(type(mytuple))

# using tuple constructor
thistuple = tuple(("fish", "cow", "rabbit", "dog", "goat", "duck", "snake"))
print(thistuple)



# Access Tuple Items
print(mytuple[1])
print(thistuple[2])



# Negative Indexing
# Negative indexing means start from the end.


print(mytuple[-1])   #last item

print(thistuple[1:-2])  # from the index 1 to the index before the last 2 -> cow - gaot


# Tuple items can be of any data type:

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(type(tuple1))


tuple2 = (True, False, True)
print(type(tuple2))


# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

#  not a tuple
tuple3 = ("fish")
print(type(tuple3))


tuple3 = ("fish",)
print(type(tuple3))



# Once a tuple is created, you cannot change its values.
# ou can convert the tuple into a list, change the list, and convert the list back into a tuple.

properties = ("house", 'car', "land")
y = list(properties)
y.append("estate")
y[1] = "school"
properties = tuple(y)

print(properties)

#  Add tuple to a tuple.

thistuple = ("apple", "banana")
z = ("cherry",)
thistuple += z
print(thistuple)



# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":


fruits = ("grape", "avocado", "carrot")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)



# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.


# Using Asterisk*


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits 

print(green)
print(yellow)
print(red) 


# Join Tuples

tuple1 = ("a", "b", "c", "d")
tuple2 = (1, 2, 3, 4)
tuple3 = tuple1 + tuple2
print(tuple3)


# Multiply Tuples
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

mytuple = fruits * 2

print(mytuple)



# Python Tuple count() Method
# Return the number of times the value 5 appears in the tuple:

thistuple = (3, 2, 3, 4, 5, 3, 5, 6, 7, 3, 5, 6, 3, 5, 3, 6, 3)
x = thistuple.count(5)   #returns the number of times 5 appears
z = thistuple.count(3) 

print(x)
print(z)


# Python Tuple index() Method
# Search for the first occurrence of the value 8, and return its position:

t = thistuple.index(4)
print(f"4 appears in index {t}")
