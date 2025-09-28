# a function that takes a list and target parameter
# multiple variables : middle, start, end, steps 
# recursion or while loop
# increase the steps each time a split is done 
# conditions to track target position 

import math

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        print(f"Step {steps} : {list[start: end+1]}")

        steps +=1
        middle =  math.floor((start + end) / 2)

        if element == list[middle]:
            return middle
        
        if element < list[middle]:
            end = middle - 1
        else:
            end = middle + 1

    return -1
            

binary_search([1, 2, 3, 4, 5, 6, 7],  10)
