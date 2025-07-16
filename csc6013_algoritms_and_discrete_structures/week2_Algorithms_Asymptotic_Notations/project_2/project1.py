"""
Title: PROJECT 1
Author: Shaun Clarke
Goal:
1) Find the number of entries in an array of integers that are divisible by a given integer.
Your function should have two input parameters – an array of integers and a positive integer – and
should return an integer indicating the count using a return statement.
Run your algorithm on the problem instances:
a) [20, 21, 25, 28, 33, 34, 35, 36, 41, 42] number of entries that are divisible by 7
and
b) [18, 54, 76, 81, 36, 48, 99] number of entries that are divisible by 9
"""

# importing dependencies
from typing import List

# This class prompts the user for an input
class UserInput:
    """
    This class does not need to be instantiated.
    It prompts the user to input an integer.
    """
    # This static method prompts the user for an int input
    @staticmethod
    def get_user_number_input() -> int:
        # While loop to prompt user until input is satisfied
        while True:
            try:
                # Prompting the user to enter an integer
                user_input: int = int(input(f"Enter a number, any number\n: ").strip())
                return user_input
            except ValueError:
                print("\nYour input must be a number\n")
    
    # This static method prompts the user to enter a list of ints
    @staticmethod
    def get_list_input() -> List:
        # Looping until input criteria has been satisfied
        while True:
            try:
                # promt user to enter a list of numbers
                user_input: List = input("\nEnter a list of comma separated numbers\n: ").strip().split(",")
                # converting all list items from stirng to int
                user_input = list(map(int, user_input))
                return user_input
            except ValueError as err:
                print(err)
                

# This class checks the divisibility of numbers in an array
class CheckDivisibility:
        
    # This method loops through an array and find the devisible numbers
    @staticmethod
    def check_divider(an_array: List, divider: int) -> int:
        # counter to hold count of divisible numbers
        div_counter = 0
        # loop through array and perform operation
        for number in an_array:
            if number % divider == 0: # if this is true
                div_counter += 1 # Increment by 1
        return div_counter
    
# This function calls the program
def main():
    
    # prompting user to input a list of numbers
    list_input = UserInput.get_list_input()
    
    # prompting user to input divisor integer
    divisor = UserInput.get_user_number_input()
    
    # check divisibility
    divisible_numbers = CheckDivisibility.check_divider(list_input, divisor)
    # formatting output and using an in line conditinal statement to pluralize
    print(f"\nThe array you entered has {divisible_numbers} number{'s' if divisible_numbers != 1 else ''} that are divisible by {divisor}.\n")

# Running program if script is invoked directly 
if __name__ == "__main__":
    main()
