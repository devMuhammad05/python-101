
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

print(myList[2:5])  # get from index 2 to 5