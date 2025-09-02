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

setOne.discard("princess")
print(setOne)





# loop sets 
countries = {"Germany", "United State", "Nigeria", "Congo"}

for country in countries:
    print(country)



# Join sets
# 1. union() and update() methods joins all items from both sets 
# 2. intersection() methods joins all items from both set 
# 3. difference() method keeps the items from the first set that are not in the other set(s) 


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() 

set3 = set1 | set2
print(set3)

# Join Multiple Sets

set4 = {"w", "x", "y", "z"}
set5 = {4, 5, 6, 7}

set6 = set4.union(set3, set4, set5)
print(set6)


# Join a Set and a Tuple

e = {"pencil", "book", "ruler"}
z = ("uniform", "shoe")

t = e.union(z)
print(t)


# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.



# Update
# The update() changes the original set, and does not return a new set.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)

print(set1)  # returns the full set because, the original set is also updated


# Note: Both union() and update() will exclude any duplicate items.



# Intersection

# Keep ONLY the duplicates

# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"x", "google", "linkedin",  "whatsapp", "instagram"}
set2 = {"google", "whatsapp", "apple", "instagram"}

set3 = set1.intersection(set2)
print(set3)


# You can use the & operator instead of the intersection()



# intersection_update

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.


set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "orange", "apple"}

set1.intersection_update(set2)
print(set1)





# Difference
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "orange", "apple"}

set3 = set1.difference(set2)    # or set1 - set 2
print(set3)
