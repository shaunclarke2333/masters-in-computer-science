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


class UserInput:
    @staticmethod
    def get_input() -> int:
        """
        - This static method prompts the user to enter a number.
        - It also keeps asking until the user enters a positive number.
        """
        while True:
            try:
                user_input: int = int(input(f"\nPlease enter a number for the knapsack capacity\nCapacity: "))

                if not isinstance(user_input, int):
                    raise ValueError
                else:
                    return user_input
                
            except ValueError as e:
                print(f"\nYou must enter a number and make sure it is a whole number")

class ProcessCSV:
    csv_data: List = [] # List to hold file content
    def __init__(self, file_name: str):
        self.file_name = file_name # CSV filename

    # This method reads a CSV and returns a list of the lines
    def read_csv(self) -> List:
        # Loading csv in memeory "as a file"
        with open(self.file_name, mode="r")as file:
            # reading the data from the file as a list of list.
            file_content = csv.reader(file)
            # looping through list of lists and ading lines to list.
            for line in file_content:
                ProcessCSV.csv_data.append(line)
            # print(f"This is csv lines: {ProcessCSV.csv_data}")
            

    # This methods generates arrays for values, cubic measurements and weight
    def generate_arrays_v_w_n(self) -> List[List]:

        # Empty lists to hold values, weight and name
        values: List = []
        weights: List = []
        names: List = []

        # Looping through csv data to create value and weight arrays
        for line in ProcessCSV.csv_data:
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

        return values, weights, names

class Knapsack:
    def __init__(self, names:List[str], v:List[int], volume:List[int], cap: int):
        self.names = names # product names
        self.v = v # product cost
        self.volume = volume # cubic measurements
        self.cap = cap # Overall capacity

    # knapsack unbounded - Greedy approach
    def knapsack(self):
        rvv = []         # triplet ratio, volume, value, index
        for i in range(len(self.v)):
            rvv.append([self.v[i]/self.volume[i],self.volume[i],self.v[i],i])
        rvv.sort(reverse=True)    # sort from high to low rate
        ans = []                     # the list of added items
        tvolume = 0                                  # total volume
        found = True
        while (found):        # until no fitting item is found
            found = False
            for t in rvv:              # search an item to add
                if (t[1] + tvolume) <= self.cap:      # if the item fits
                    ans.append(t[3])                  # add it
                    tvolume += t[1]
                    found = True
                    break
        return ans           # returns the list of added items
    
    def process_knapsack_output(self, output):
        print(f"\n{output}")
        # Dictiondary to hold data for each item selected to fill the capacity
        label_dict:Dict = {}
        for i in output:
            # if the name of an item is not in the dict add it
            if self.names[i] not in label_dict:
                # adding the item name as a key along with index, how many times the item was added, the cost, and the cubic measurement.
                label_dict[self.names[i]] = [i, 1, self.v[i], self.volume[i]]
                # print(label_dict[names[i]][1])
                # If the item already exists then increment the number of times it was added tot he knapsack.
            elif self.names[i] in label_dict:
                # print(f"{i} is in label dict")
                # Incrementing item count
                label_dict[self.names[i]][1] += 1

        # empty list to hold the item names an info as list of lists
        data: List = []
        # looping through dictinary and adding the key(name) to the beginning of the list of values.
        for key, value in label_dict.items():
            # adding they key as the first item in the list of values
            value.insert(0, key)
            # print((value))
            # adding the updated value list to the data list
            data.append(value)
            # print(data)
        
        return data


def main():

    # Prompting user for capacity
    cap = UserInput.get_input()
    # Instantiating ProcessCSV object with filename
    get_data = ProcessCSV("packs3.csv")
    # reading data from csv
    get_data.read_csv()
    # Generating arrays with values, volume etc from each line of csv data
    values, weights, names = get_data.generate_arrays_v_w_n()
    # Instantiating knapsack object
    knapsack = Knapsack(names, values, weights, cap)
    # calling knapsack method
    output = knapsack.knapsack()
    # process output data from knapsack
    data = knapsack.process_knapsack_output(output)
            

    if len(data) == 1:
        name: str = data[0][0]
        num_of_items:  int = data[0][2]
        total: int = num_of_items * data[0][3]
        used_space: int = num_of_items * data[0][4]
        unused_space: int = cap - used_space
        
        print(f"The suggested items are: {num_of_items}, {name}, with a total of ${total}.")
        print(f"There were {unused_space} cubic inches left") 

    elif len(data) > 1:
        name1: str = data[0][0]
        name2: str = data[1][0]
        num_of_items1: int = data[0][2]
        num_of_items2: int = data[1][2]
        total1: int = num_of_items1 * data[0][3]
        total2: int = num_of_items2 * data[1][3]
        overall_total: int = total1 + total2
        used_space: int = (num_of_items1 * data[0][4]) + (num_of_items2 * data[1][4])
        unused_space : int= cap - used_space
        print(f"\nThe suggested items are: {num_of_items1} {name1} and {num_of_items2} {name2}, with a total value of ${overall_total}.")
        print(f"There were {unused_space} cubic inches left unused.")

if __name__ == "__main__":
    main()
