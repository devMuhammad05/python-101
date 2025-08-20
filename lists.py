
# Lists are used to store multiple items in a single variable
myList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(myList)
print(len(myList))


# using the list() constructor when creating a new list.
list1 = list(("abc", 34, True, 40.6, "male"))  # note the double round-brackets
print(list1)



# Access Items
print(myList[0])  #index 0 item 
print(myList[-1]) #last index element

print(myList[2:5])   # get elements starting at index 2 up to (but not including) index 5 → effectively returns items at indices 2, 3, and 4

print(myList[0:-3])  # get elements starting at index 0 up to (but not including) the element 3 positions from the end

print(myList[:4])    # get elements from the beginning up to (but not including) index 4 → effectively returns items at indices 0, 1, 2, and 3


# check if item exist 

print("orange" in myList)

if "cherry" in myList:
    print(f"cherry is present in {myList}")


# change item value

thislist = ["apple", "banana", "cherry", "kiwi"]
thislist[1] = "blackcurrant"
print(thislist)


# Change a Range of Item Values

thislist[1:3] = ["orange", "watermelon"]
print(thislist)  # new list becomes ['apple', 'orange', 'watermelon', 'kiwi']


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]   # replace between index 1 and 2
print(thislist)



#  Add List Items

# append adds a new item to the end of the list
products = ["shoe", "bags", "chair", "table"]
products.append("laptop")
print(products)


# insert items
products.insert(1, "mouse")
print(products)


# extend list 
# To append elements from another list to the current list, use the extend() method. like merging list

more_products = ["keyboard", "cables", "books", "phones"]
products.extend(more_products)
print(products)


# Remove Specified Item

products.remove("phones")
print(products)

# Remove Specified Index
products.pop()  # removes last element
print(products)


products.pop(0)  # removes element in the index 0
print(products)


# The del keyword also removes the specified index:

del products[0]
print(products)


# The del keyword can also delete the list completely.
del more_products   #deletes the entire more_products list that was extended to products
print(products)   


