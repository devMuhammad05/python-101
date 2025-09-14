def count_words_and_lines(filename): 
    try:
        with open(filename) as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)

            print(f"Total lines: {line_count}")
            print(f"Total words: {word_count}")

    except FileNotFoundError:
        print(f"File {filename} not found!")
    

count_words_and_lines("demofile.txt")



def write_item_to_file(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")

def read_items_from_file(filename):
    try:
        with open(filename) as file:
            items = file.readlines()
            print("Items in the file")
            for item in items:
                print(item.strip())

    except FileNotFoundError:
        print(f"File {filename} not found!")



items = ["Apple", "Banana", "Cherry", "Grapes"]
write_item_to_file("newfile.text", items)


read_items_from_file("newfile.text")



# additional practice 
# write a program to copy the content of one file to another 
#  first open the file, read, the content then write to another file 