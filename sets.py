# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Once a set is created, you cannot change its items, but you can remove items and add new items, and it does not allow duplicate items.




newset = {"apple", "banana", "cherry"}
print(newset)



# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)



# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

newset = {"book", "watch", 1, True}
print(newset)


# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:




# Access Set Items
# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

for x in newset:
    print(x)


# check if item is present in set
print("house" in thisset)
print("banana" in thisset)


# Add Items to set 
newset.add("orange")

print(newset)


# Add Sets
# To add items from another set into the current set, use the update() method.


fruit1 = {"apple", "banana", "orange"}
fruit2 = {"pineapple", "mango", "papaya"}

fruit1.update(fruit2)

print(fruit1)



# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

setOne = {"king", "queen"}
listOne = ["prince", "princess"]

setOne.update(listOne)
print(setOne)





# Remove Set Items
#  using .remove() or .discard()  or .pop()

setOne.remove("prince")
print(setOne)


setOne.remove("king")
print(setOne)

