
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:


with open("demofile.txt", "r+") as file:
    content = file.read()

    print(content)



# specify numbers of characters

with open("demofile.txt") as file:
    content = file.read(10)
    print(content)


# Read Lines
# You can return one line by using the readline() method:

with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())


# By looping through the lines of the file, you can read the whole file, line by line:

with open("demofile.txt") as file:
    for line in file:
        print(line)


# Write to an Existing File
# "a" - Append - will append to the end of the file

with open("demofile.txt", "a") as file:
    file.write("\n Now the file has more content") 

#open and read the file after the appending:

with open("demofile.txt") as f:
    print(f.read())



# "w" - Write - will overwrite any existing content

# with open("demofile.txt", "w") as file:
#     file.write("\n Now the file has been overwritten") 


# with open("demofile.txt") as f:
#     print(f.read())




# "x" - Create - will create a file, returns an error if the file exists
# file error handling

try:
    with open("myfile.txt", "x") as file:
      file.write("Hello, world!")
except FileExistsError:
    print("File already existed")


try:
    with open("file.txt") as file:
      print(file.read())
except FileNotFoundError:
    print("File not found")

