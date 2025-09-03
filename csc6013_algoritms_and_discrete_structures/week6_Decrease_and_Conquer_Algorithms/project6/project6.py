"""
Develop one Python program to perform the Quick Select algorithm and for an array of n elements it should find the k-th smallest element of the array).
Inspire yourself by the video example that needs to be adapted by yourself.

You must code a function QuickSelect that receives an array and the element the user wants to find (k-th smallest);
Then the main function of your program should generate a random array of 1000 elements to be searched, ask the user the value of k, call QuickSelect, and display the searched element found.
"""

from typing import List
import random

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
                

class GenerateArray:
    """
    This class does not need to be instantiated.
    It prompts the user to input an integer.
    """

    @staticmethod
    def generate_random_array(size=1000, low=1, high=1000) -> List:
        # Create an empty list to hold the random numbers
        random_array: List = []

        # Looping to generate and append the numbers to the array.
        for _ in range(size):
            # Selecting a random integer between the low and high makers and appending it
            random_array.append(random.randint(low, high))

        # return the completed list of random numbers
        return random_array

class QuickSelect:
    def __init__(self, numbers: List[int], k: int):
        # The list of numbers
        self.numbers = numbers
        # The k-th smallest we are looking for
        self.k = k
    
    # This method finds the k-th smallest number
    def find_k_smallest(self) -> int:
        
        nums = self.numbers
        
        target = self.k - 1  # K-th smallest -> index K-1

        def quickselect(l: int, r: int) -> int:
            # sleecting the last element in the current range as pivot
            pivot: int = nums[r]
            # Pointer p to keep track of where the pivot will finally go
            p: int = l
            # Looping from left to right 
            for i in range(l, r):
                # If the current number is smaller than the pivot
                if nums[i] < pivot:
                    # Swap it with the element at pointer p
                    nums[p], nums[i] = nums[i], nums[p]
                    # Move pointer forward
                    p += 1
            # Moving the pivot into its correct final spot
            nums[p], nums[r] = nums[r], nums[p]  

            # If pivot is to the right of the target index, check the left side
            if p > target:
                return quickselect(l, p - 1)
            # If pivot is to the left of the target index, check the right side
            elif p < target:
                return quickselect(p + 1, r)
            # If pivot is at the target index then return kth smallest element
            else:
                return nums[p]

        # Make sure k is within range so it is valid
        if not 1 <= self.k <= len(nums):
            raise ValueError("k is out of range")

        # Calling quickselect and returning the array
        return quickselect(0, len(nums) - 1)

def main():
    
    # Generating the array
    num_array: List = GenerateArray.generate_random_array()
#     print(num_array[0:30])
    
    # Asking for user input
    user_input: int = UserInput.get_user_number_input()
    
    # Instantiating the QuickSelect class
    find_kth_smallest = QuickSelect(num_array, user_input)
    
    result = find_kth_smallest.find_k_smallest()
    
    print(f"The {user_input}-th smallest element is: {result}")


if __name__ == "__main__":
    main()