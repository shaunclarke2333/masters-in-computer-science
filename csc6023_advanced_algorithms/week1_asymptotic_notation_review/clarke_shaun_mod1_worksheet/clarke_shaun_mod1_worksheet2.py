"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 1 Asymptotic Notation Review
Task:
    Worksheet Task 02
    Extend the program of Task #1 to output not only the maximum value, but also the initial and final index of the elements to compute the maximum value
    Go to IDLE and try to program it
"""

"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 1 Asymptotic Notation Review
Task:
    Worksheet Task 01
    Create a program that randomizes a vector of 1000 positive and negative integers, then finds the maximum contiguous subsequence sum value
    Prints out the maximum value
"""

from typing import List
import random


class MaxContSubSum:
    def __init__(self, a: List[int]):
        self.a = a
    # Maximum Contiguous Subsequence Sum method
    
    def MCSS(self) -> int:
        """
        This static method caclculates the maximum contiguous subsequence sum of an array.
        """
        # declaring variables for counter, largest sum and i.
        largest, acc, i = 0, 0, 0
        # looping the array to find the largest sub sequence
        for j in range(len(self.a)):
            print(f"This is J: {j}")
            # Incrementing acc by the next item in the list.
            acc += self.a[j]
            print(f"This is acc: {acc}\n")
            # If the number or numbers summed so far is greater than largest, update largest with acc.
            if (acc > largest):
                largest = acc
                print(f"This is largest: {largest}\n")
            elif (acc < 0): # if acc is negative reset it to 0.
                i = j + 1
                acc = 0
        return largest


class RandomVector:

    # This static method generates an array with 1000 positive and negative integers 
    @staticmethod
    def generate_array():
        """
        This static method generates an array with 1000 positive and negative integers. 
        """
        # empty list to hold generated numbers
        a = []
        # declaring start and stop variables for the random number range
        start, stop = -1000, 1000
        # looping through and generating 1000 + and - ints
        for i in range(stop):
            a.append(random.randint(start, stop))
        
        return a


# This main method calls the program
def main(RandomVector: RandomVector, MaxContSubSum: MaxContSubSum) -> int:
    """
    This method calls the program
    """
    # Calling the static method to generate the array
    array: List = RandomVector.generate_array()

    # print(f"{array[:10]}")
    # a = [2,3, -4, -5,5,6,7]
    # a = [5, -1, 56, -3, -18, 22, -9]

    # Instantiating the MaxContSubSum class with the generated array
    sub_sum = MaxContSubSum(array)
    print(f"{sub_sum.MCSS()}")

if __name__ == "__main__":
    main(RandomVector, MaxContSubSum)
