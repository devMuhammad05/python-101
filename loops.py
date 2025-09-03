

# For Loops
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)


for number in range(3):
    print("Python", number, number * ".")


for number in range(1, 5):
    print("Attempting", number, number * ".")


# third argument as step
for number in range(1, 10, 2):
    print("Attempting", number, number * ".")


# breaking out of a loop

# successful = True
successful = False
for number in range(3):
    print("Sending")
    if successful:
        print("Attempt Successful")
        break
    else:
        print("Attempted 3 times and failed")


for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


fruits = ["apple", "banana", "cherry", "mango", "pineapple"]

for fruit in fruits:
    print(fruit)

for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        # print("banana is present")
        break


# The continue Statement
products = ["shoe", "bags", "chair", "table"]

for product in products:
    if product == "bags":
        continue
    print(product)


for number in range(2, 5):
    print(number)  # 2-4


for number in range(2, 30, 3):
    print(number)  # 2, 5, 8 - 29


# The pass Statement

for x in [0, 1, 2, 3, 4, 5]:
    pass


# Loop Through a Tuple

thistuple = ("apple", "banana", "cherry")

for fruit in thistuple:
    print(fruit)


# Loop Through the Index Numbers

for fruit in range(len(thistuple)):
    print(thistuple[fruit])


# while loop

products = ("laptop", "generator", "AC", "Desktop")
i = 0
while i < len(products):
    print(products[i])
    i += 1



# Loop Through a Dictionary

thisdict = {
    "fruit" : "banana",
    "laptop" : "dell",
    "social_media" : "linkedin",
    "food" : "rice",
}

# print all key names: fruit, laptop etc
for x in thisdict:
    print(x)

# print all values: banana, dell etc
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)


# loop through both keys and values 

for x, y  in thisdict.items():
    print(x, y)