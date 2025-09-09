def greet(first_name, last_name):
    print("Hi there")
    print(f"Welcome aboard {first_name} {last_name}")

greet("Muhammad", "Yahaya")


def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Starman")
print(message)


def increment(number, by):
    return number + by

result = increment(2, by=5)
print(result)



# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

def multiply(*numbers):
    total = 1
    for number in numbers:
         total *= number
    return total

print(multiply(2, 3, 4, 5))


def get_kid_name(*kids):
    print("The child name is " + kids[2])


get_kid_name("Emil", "Tobias", "Linus")




# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.


def get_fruit_with_longest_name(fruits):

    longest_fruit_name = fruits[0]

    for fruit in fruits:
        if len(fruit) > len(longest_fruit_name):
            longest_fruit_name = fruit
    
    print(longest_fruit_name)


fruits = ["apple", "pineapple", "cherry"]

get_fruit_with_longest_name(fruits)



def get_shortest_fruit_name(fruits):
    shortest_fruit_name = fruits[0]

    for fruit in fruits:
        if len(fruits) < len(shortest_fruit_name):
            shortest_fruit_name = fruit

    print(shortest_fruit_name)

fruits = ["apple", "pineapple", "cherry", "pawpaw"]

get_shortest_fruit_name(fruits)



def get_most_frequent_words(words):
    words_and_count = {}

    for word in words:
        if word in words_and_count:
            words_and_count[word] += 1   # increment count
        else:
            words_and_count[word] = 1    

    # find the maximum count
    max_count = max(words_and_count.values())

    # collect all words that match the maximum count
    most_frequent = [word for word, count in words_and_count.items() if count == max_count]

    print("Word counts:", words_and_count)
    print("Most frequent word(s):", most_frequent)


words = ["abc", "dec", "edc", "rtc", "ett", "dec", "dee", "dec"]
get_most_frequent_words(words)
