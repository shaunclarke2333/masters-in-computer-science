"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 3 Greedy Algorithms
Project Assignment:
    Create a program that receives the list of possible named items with the following information:

    ○ Value ($), Height (in), Width (in), Depth (in)

    The limit of the optimal solution is expressed by the volume in cubic inches (in3) and the program has to maximize the value within the cubic limit
    Your program should read a textual file with one item type per line with the information separated by comma, for example this fileLinks to an external site. 
    lists four items with values 35, 40, 45, and 58 dollars and increasing dimensions
    Your program should capture the overall limit of the package/knapsack from the user.
    Your program should read any file with this format (name, value, height, width, depth) per line
    Your program must print out the best distribution with a string like: "The suggested items are: 72 Milky Ways and 5 Tootsie Rolls with a total value of $53. There were 4 square inches left unused."
    The printed statement must at least include: names of items included; number of items included; total profit; leftover space.

    Mod 3 test case
    Hamburgers,3,2,4,4
    Hot Dogs,1,1,1,6
    Sausages,2,2,2,6
    Veggie Burgers,4,2,3,3

    ---------

    If you put the capacity as 500 the results should be:

    The suggested items are: 27 Veggie Burgers and 2 Hot Dogs, with a total value of $110.
    There were 2 cubic inches left unused.
"""

from typing import List
from typing import Dict
import csv

def read_csv(file_name: str) -> List:
    # List to hold file content
    csv_data: List = []
    # Loading csv in memeory "as a file"
    with open(file_name, mode="r")as file:
        # reading the data from the file as a list of list.
        file_content = csv.reader(file)
        # looping through list of lists and ading lines to list.
        for line in file_content:
            csv_data.append(line)
        return csv_data


csv_data = read_csv("packs1.csv")
# Empty lists to hold values and weight
values: List = []
weights: List = []
names: List = []

# Looping through csv data to create value and weight arrays
for line in csv_data:
    name: str = line[0]
    cost: int = int(line[1])
    # print(type(int(line[2])))
    cubic_inches: int = int(line[2]) * int(line[3]) * int(line[4])
    # adding cost to list
    values.append(cost)
    # adding weight to list
    weights.append(cubic_inches)
    # adding names to list
    names.append(name)

# print(f"names: {names}\nvalues: {values}\nweights: {weights}")

# knapsack unbounded - Greedy approach

def knapsack(v, w, cap):
    rwv = []         # triplet ratio, weight, value, index
    for i in range(len(v)):
        rwv.append([v[i]/w[i],w[i],v[i],i])
    rwv.sort(reverse=True)    # sort from high to low rate
    ans = []                     # the list of added items
    tw = 0                                  # total weight
    found = True
    while (found):        # until no fitting item is found
        found = False
        for t in rwv:              # search an item to add
            if (t[1] + tw) <= cap:      # if the item fits
                ans.append(t[3])                  # add it
                tw += t[1]
                found = True
                break
    return ans           # returns the list of added items

"""
The suggested items are: 27 Veggie Burgers and 2 Hot Dogs, with a total value of $110.
There were 2 cubic inches left unused.
"""
cap = 500
output = knapsack(values, weights, cap)
print(output)
label_dict:Dict = {}
for i in output:
    if names[i] not in label_dict:
        label_dict[names[i]] = [i, 1, values[i], weights[i]]
        # print(label_dict[names[i]][1])
    elif names[i] in label_dict:
        # print(f"{i} is in label dict")
        label_dict[names[i]][1] += 1


# print(label_dict)
# print(len(label_dict))

data: List = []
for key, value in label_dict.items():
    value.insert(0, key)
    # print((value))
    data.append(value)
    # print(data)
    

if len(data) == 1:
    name = data[0][0]
    num_of_items = data[0][2]
    total = num_of_items * data[0][3]
    used_space = num_of_items * data[0][4]
    unused_space = cap - used_space
    
    print(f"The suggested items are: {num_of_items}, {name}, with a total of ${total}. There were {unused_space} cubic inches left")

elif len(data) > 1:
    name1 = data[0][0]
    name2 = data[1][0]
    num_of_items1 = data[0][2]
    num_of_items2 = data[1][2]
    total1 = num_of_items1 * data[0][3]
    total2 = num_of_items2 * data[1][3]
    overall_total = total1 + total2
    used_space = (num_of_items1 * data[0][4]) + (num_of_items2 * data[1][4])
    unused_space = cap - used_space
    print(f"The suggested items are: {num_of_items1} {name1} and {num_of_items2} {name2}, with a total value of ${overall_total}. There were {unused_space} cubic inches left unused.")