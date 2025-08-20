
a = 33
b = 200

if b > a:
    print(f"{b} is greater than than {a}")


# Elif
z = 33
t = 33

if z > t:
    print(f"{z} is greater than than {t}")
elif z == t:
    print(f"{z} is equal to {t}")



# Short Hand If
if a < b:  print(f"{a} is less than than {b}")


# Short Hand If ... Else
print("A is lesser") if a < b else print("B is lesser") 


# logical operators - and, or, not

a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are true")


if not b > a:
    print("b is NOT greater than a")



age = 22


# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")

# short if else || Ternary Operator
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)



# age should be between 18 and 65
if age >= 18 and age < 65:
    print("Eligible")


print(10 == "10")    #false - it handles it like strict comparison 


# It uses the Unicode (ASCII) code point values of the characters.
# ompare first letters:

# "b" → Unicode 98

# "a" → Unicode 97

# Since 98 > 97, Python decides "bag" > "apple" is True right away.

# It doesn’t even need to look at the next letters ("a" vs "p") because the result is already determined by the first mismatch.

print("bag" > "apple")  


if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat"
    print("b")
else: 
    print("c")