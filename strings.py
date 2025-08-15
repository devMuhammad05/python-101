course_name = "  Python Programming"
print(len(course_name))
print(course_name[0])  # first character
print(course_name[-1])  # first character from the end
print(course_name[0:3])  # start from index 0 to 3
print(course_name[:3])  # start from index 0 to 3
print(course_name[5:])  # start from index 5 to the last
print(course_name[:])  # original copy of string


first = "Muhammad"
last = "Yahaya"

full = first + " " + last
print(full)


full_name = f"{first} {last}"
print(full_name)


total_fullname_string = f"{len(first)} {4 + 5}"
print(total_fullname_string)

print(course_name.upper())
print(course_name.lower())
print(course_name.title())

print(course_name.strip())  # remove white space

print(course_name.find("thon"))  # get index of word

print(course_name.replace("P", "K"))

print("php" not in course_name)
