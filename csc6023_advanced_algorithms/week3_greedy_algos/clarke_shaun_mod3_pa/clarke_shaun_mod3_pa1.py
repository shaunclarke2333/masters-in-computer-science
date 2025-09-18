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
import csv

# Loading csv in memeory "as a file"
with open("packs.csv", mode="r")as file:
    # reading the data from the file as a list of list.
    csv_file = csv.reader(file)
    # looping through list of lists and printing each line
    for line in csv_file:
        for i in range(len(line)):
            print(line)
            print(line[i])

    