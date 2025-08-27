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
