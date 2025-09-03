
# Dictionaries are used to store data values in key:value pairs.
# Dictionary items are ordered, changeable, and do not allow duplicates.


thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)
print(len(thisdict))





# The values in dictionary items can be of any data type:


thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "colours" : ["red", "white", "blue"]
}

print(thisdict)


# Python - Access Dictionary Items

print(thisdict["year"])
print(thisdict.get("model"))

# get keys 

print(thisdict.keys())

print(thisdict.values())


# get items 
# The items() method will return each item in a dictionary, as tuples in a list.


print(thisdict.items())


if "model" in thisdict:
    print("Yes, 'model' is a key in the thisdict dictionary")


# Change Values

thisdict["year"] = 2025
print(thisdict)


# Update Dictionary

thisdict.update({"country" : "Nigeria"})
thisdict.update({"brand" : "Mercedes"})
print(thisdict)


# Removing items 
# pop() - removes ite  with specified key name 

thisdict.pop("country")
print(thisdict)


# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)


# The del keyword removes the item with the specified key name:
# the del keyword can also delete the dictionary completely:

del thisdict['year']
print(thisdict)


# Copy a Dictionary
# using .copy() and dict()

mydict = thisdict.copy()
print(mydict)

mydict = dict(mydict)
print(mydict)



# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.


child4 = {
    "name" : "John",
    "year" : 2008
}

family = {
    "child1" : {
        "name" : "Emil",
        "year" : 2005
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },   
    "child3" : {
        "name" : "linus",
        "year" : 2011
    },  
    "child4" : child4  
}


print(f"family child2 name {family['child2']['name']}")

print(f"family child4 year {family['child4']['name']}")