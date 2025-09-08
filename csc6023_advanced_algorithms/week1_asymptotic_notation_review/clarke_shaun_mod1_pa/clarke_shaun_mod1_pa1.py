"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 1 Asymptotic Notation Review
Project Assignment Part 1:
    Instructions
    Create a program that implements a sort algorithm of your choice and applies it to a random vector of 1,000 elements
    Repeat the process applying it to random vectors of 2,000, 3,000, ... up to 10,000 elements
    Compute the time complexity of your algorithm and verify if the time it takes to your 1,000 to 10,000 corresponds to the time complexity prediction. You should use CProfile to record how long the sorting takes for each array. 
    Besides the implementation of your program, write a short report describing your experiences and conclusion. Your report must include the following points:

    big oh class of the sorting algorithm in question, with an explanation
    screenshots of the C Profiler
    graph plotting the size of the random arrays (x axis) and the time taken to sort (y axis)
    your reflections on how the C Profile data relates to what you have learned about algorithmic analysis and in particular to the big oh class of your algorithm.

    Sorting algorithm:
    bubble
    select
    insertion

"""
from typing import List
import random
import cProfile

def bubble_sort(array: List[int]) -> List:
    # This variable will break the loop once the list has been sorted
    sorted: bool = False

    # looping until list is soreted
    while not sorted:
        # setting sorted to true so it will break the loop
        sorted: bool = True
        # looping for the length of the unsorted array
        for i in range(0, len(array) - 1): # minus 1 because the last number of the list has nothing to compare to.
            # if the num to the left is greater than the num to the right update sorted to false.
            if array[i] > array[i+1]:
                sorted: bool = False
                # sort the num on the left and on the right by swapping them.
                array[i], array[i+1] = array[i+1], array[i]

    return array

# a = [4,3,5,1,3,2]

# print(bubble_sort(a))

def generate_array() -> List:
    """
    This static method generates an array with 1000 positive and negative integers. 
    """
    # empty list to hold generated numbers
    a: List = []
    # declaring start and stop variables for the random number range
    start, stop = 1, 1000
    # looping through and generating 1000 + and - ints
    for i in range(stop):
        a.append(random.randint(start, stop))
    
    print(f"This is the first 10 of the array after sorting: {a[:10]}")
    return a

# print(f"{len(generate_array())}")

# if __name__ == "__main__":
#     cProfile.run("main()")

# print(f"{bubble_sort(generate_array()[:10])}")
array = generate_array()
# print(f"This is the first 10 of the array before sorting: {array[:10]}")
array[:10]
cProfile.run("bubble_sort(array)")


