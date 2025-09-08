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


def generate_arrays() -> List:
    # Empty list to hold range for random vectors
    random_vector_lists: List = []

    # Generating range for vectors
    for r in range(1000,11000,1000):
        # empty array to hold generated numbers
        array = []
        for i in range(r):
            
            # Starting variable where random vector range starts
            start: int = 1
            # Adding randomly generated numbers to list
            array.append(random.randint(start, r))
            
        # adding randomly generated array to list of lists.
        random_vector_lists.append(array)
    
    return random_vector_lists

# Generating list of arrays from 1000, to 10,000
arrays = generate_arrays()

def main():
    """
    This function runs the program
    """

    print(f"array {len(array)} first five before sort: {array[:5]}")
    
    # sorting each array
    sorted_array = bubble_sort(array)
    print(f"array {len(sorted_array)} first five after sort: {sorted_array[:5]}")


if __name__ == "__main__":
    # Looping through each array and calling bubble sort on each with cProfile
    for array in arrays:
        # calling main with cProfile
        cProfile.run("main()")