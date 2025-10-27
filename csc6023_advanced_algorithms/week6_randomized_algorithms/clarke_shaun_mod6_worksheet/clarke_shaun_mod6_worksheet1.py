"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 6 Randomized Algorithms
Task:
    Worksheet Task 01
    
    Create a program that generates a random array of 10,000 elements with equal number of 0's and 1's and then implement the randomized Las Vegas algorithm that searches for an element holding a 1

    Your program should output the position of the first 1 found, plus the number of tries before finding it.
"""

from typing import List
import random


class GenerateArrays:
    # This method generates a list with a specific count of a number
    @staticmethod
    def generate_list_of_nums(num: int, total_items: int) -> List[int]:
        # number of items to generate
        number_of_items: int = total_items
        # Generating list of items
        list_of_itemss: List[int] = [num] * number_of_items
        return list_of_itemss

class ArrayTools:
   
    def __init__(self, array1: List[int], array2: List[int]):
        self.array1: List[int] = array1
        self.array2: List[int] = array2
        self.joined_array: List[int] = []

    # This method joins two lists
    def join_lists(self) -> List[int]:
        # Joining lists
        self.joined_array: List[int] = self.array1 + self.array2

    # This method shuffles the list.
    def shuffle_list(self) -> List[int]:
        # Shuffling joined list.
        random.shuffle(self.joined_array)
    
    # This method creates a list of list with each item in the array paired with its index.
    def pair_item_and_index(self) -> List[List[int]]:
        for i in range(0, len(self.joined_array)):
            # replacing item at index with a list containing the item and index.
            self.joined_array[i] = [self.joined_array[i], i]

        return self.joined_array

class VivaLasVegas:
    # This method uses the las vegas approach to find the first 1 in a n array
    @staticmethod
    def vegas_baby(ten_k_array: List[List[int]]):
        # keep track of attempts
        count_attempts = 0
        while True:
            selection = random.choice(ten_k_array)
            # print(selection)
            # counting selection attempt
            count_attempts += 1
            # getting the selected item from its sublist
            item = selection[0]
            
            if item == 1:
                # getting the selected item's index from the sublist
                item_index = selection[1]

                return item, item_index, count_attempts

def main():
    

    # ones = [0,0,0,0,0,0,]
    # zeroes = [1,1,1,1,1,1]

    # generating 5000 1's and 0's
    ones = GenerateArrays.generate_list_of_nums(1, 5000)
    zeroes = GenerateArrays.generate_list_of_nums(0, 5000)

    # Instantiating ArrayTools class
    array_tools = ArrayTools(ones, zeroes)

    # joining lists
    array_tools.join_lists()

    # Shuffling joined list
    array_tools.shuffle_list()

    # pairing items in list with it's index.
    shuffled_list = array_tools.pair_item_and_index()

    # print(shuffled_list)

    # Lets roll the dice and try our luck in vegas
    item, item_index, count_attempts = VivaLasVegas.vegas_baby(shuffled_list)

    print(f"It took {count_attempts} attempts to find the first {item} at index {item_index}")


if __name__ == "__main__":
    main()
