"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 1 Asymptotic Notation Review
Task:
    Worksheet Task 02
    Extend the program of Task #1 to output not only the maximum value, but also the initial and final index of the elements to compute the maximum value
    Go to IDLE and try to program it
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
        # empty list to hold indexes
        index_list = []
        # empty variable to hold final list
        final_list = ""
        # declaring variables for counter, largest sum and i.
        largest, acc, i = 0, 0, 0

        # looping the array to find the largest sub sequence
        for j in range(len(self.a)):
            # print(f"This is J: {j}")
            # Incrementing acc by the next item in the list.
            acc += self.a[j]
            # adding the index to list every time acc is incremented
            index_list.append(j)
            # print(f"This is index list: {index_list[:10]}\n")
            # If the number or numbers summed so far is greater than largest, update largest with acc.
            if (acc > largest):
                largest = acc
                # Making a copy of final list if acc is presently the largest
                final_list = index_list.copy()
                # print(f"This is largest: {largest}\n")
            elif (acc < 0): # if acc is negative reset it to 0.
                i = j + 1
                acc = 0
                # clearing the list if acc is negative, this means a new set of indexes will be incremented.
                index_list.clear()

        # Getting first index and last index from final list
        start_index: int = final_list[0]
        end_index: int = final_list[-1]
        return largest, start_index, end_index


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
    # a = [-2 , 11, -4, 13, -5, 2]
    # a = [5, -1, 56, -3, -18, 22, -9]

    # Instantiating the MaxContSubSum class with the generated array
    sub_sum = MaxContSubSum(array)
    # unpacking the MCSS method output.
    largest, start, end = sub_sum.MCSS()

    print(f"The maximum Contiguous Subsequence Sum is {largest}.")
    print(f"The initial index is {start} the final index is {end}.")

if __name__ == "__main__":
    main(RandomVector, MaxContSubSum)
