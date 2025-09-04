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


# Maximum Contiguous Subsequence Sum Function
def MCSS(a: List[int]) -> int:
    """
    """
    # declaring variables for counter, largest sum and i.
    largest, acc, i = 0, 0, 0
    # looping the array to find the largest sub sequence
    for j in range(len(a)):
        print(f"This is J: {j}")
        # Incrementing acc by the next item in the list.
        acc += a[j]
        print(f"This is acc: {acc}\n")
        # If the number or numbers summed so far is greater than largest, update largest with acc.
        if (acc > largest):
            largest = acc
            print(f"This is largest: {largest}\n")
        elif (acc < 0): # if acc is negative reset it to 0.
            i = j + 1
            acc = 0
    return largest


# a = [2,3, -4, -5,5,6,7]
# a = [5, -1, 56, -3, -18, 22, -9]

# empty list to hold generated numbers
a = []
# declaring start and stop variables for the random number range
start, stop = -10, 10
# looping through and generating 1000 ints
for i in range(stop):
    a.append(random.randint(start, stop))

print(a)

print(f"{MCSS(a)}")


