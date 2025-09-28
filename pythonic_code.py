# Pythonic codes
# Pythonic code means writing code that follows the style, idioms, and conventions of Python — code that feels natural to Python programmers.


# [expression for item in interable if condition]
# expression → what you want to compute/store for each item

# item → variable representing each element in the iterable

# iterable → any sequence (list, tuple, string, range, etc.)

# if condition → optional filter (only include items that satisfy this condition)




squares = [x**2 for x in range(10)]

print(squares)

even_numbers = [x for x in range(30) if x % 2 == 0]
print(even_numbers)