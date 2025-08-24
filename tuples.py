
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