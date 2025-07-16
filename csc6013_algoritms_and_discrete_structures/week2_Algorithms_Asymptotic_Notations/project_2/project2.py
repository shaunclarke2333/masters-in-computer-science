"""
Title: PROJECT 2
Author: Shaun Clarke
Goal:
Given an array of real numbers, without sorting the array,
find the smallest gap between all pairs of elements (for an array A,
the absolute value of the difference between elements 𝐴[i] and 𝐴[𝑗]).
Your function should have one input parameter – an array of numbers –
and should return a non-negative number indicating the smallest gap using a return statement.
Run your algorithm on the problem instances:
a) [50, 120, 250, 100, 20, 300, 200]
b) [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]
"""

# importing dependencies
from typing import List
import itertools

# This class prompts the user for an input
class UserInput:
    """
    This class does not need to be instantiated.
    It prompts the user to input a list of real numbers comma seperated.
    """

    # This static method prompts the user to enter a list of ints
    @staticmethod
    def get_list_input() -> List:
        # helper function to convert list items to numbers
        def to_number(s):
            try:
                # if its a int
                return int(s)
            except ValueError:
                # if its a float
                return float(s)
            
        # Looping until input criteria has been satisfied
        while True:
            try:
                # promt user to enter a list of numbers
                user_input: List = input("\nEnter a list of comma separated numbers\n: ").strip().split(",")
                # converting all list items from stirng to int
                user_input = list(map(to_number, user_input))
                return user_input
            except ValueError as err:
                print(err)
                
# This class creates unique pairs from a list of numbers
class UniquePairs:
    # This method creates unique pairs from array of numbers
    @staticmethod
    def create_pairs(an_array: List) -> int:
        # using itertools combination method to generate unique pairs from the array
        unique_pairs = list(itertools.combinations(an_array, 2))
        return unique_pairs

# This class finds the smallest gap between all pairs of entered elements
class FindSmallestGap:
    
    # finding smallest gap
    @staticmethod
    def find_smallest_gap(an_array: List) -> int:
        # Variabel to hold smallest gap
        smallest_gap = 1000
        # generating unique pairs
        for pair in an_array:
            # first and second number in pair
            first_number = pair[0]
            second_number = pair[1]
            # making sure we always subtract from the larger number
            if first_number < second_number:
                # subtracting to get the gap
                gap = second_number - first_number
                # checking if gap is smaller than what we have saved
                if gap < smallest_gap:
                    smallest_gap = gap
            else:
                # subtracting to get the gap
                gap = first_number - second_number
                # checking if gap is smaller than what we have saved
                if gap < smallest_gap:
                    # updating  smallest gap variable
                    smallest_gap = gap 
                    
        return smallest_gap

# This function calls the program
def main():
    
    # prompting user to input a list of numbers
    list_input = UserInput.get_list_input()
    
    # creating unique pairs of numbers
    unique_pairs = UniquePairs.create_pairs(list_input)

    # Finding the smallest gap in the array of pairs
    smallest_gap = FindSmallestGap.find_smallest_gap(unique_pairs)
    
    # formatting output and using an in line conditinal statement to pluralize
    print(f"\nThe smallest gap in the array you entered is {smallest_gap}.\n")

# Running program if script is invoked directly 
if __name__ == "__main__":
    main()
