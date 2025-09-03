# Exercise write a program that takes an input and returns the list of even numbers in it 

number_input = input(">")
total_even_numbers = 0

for x in range(0, int(number_input), 2):
    print(x)
    total_even_numbers +=1

print(f"Total even number is {total_even_numbers}")


