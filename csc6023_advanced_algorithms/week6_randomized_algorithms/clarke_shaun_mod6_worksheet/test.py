# --- reuse from your code (with original comments restored) ---
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
        return self.joined_array

    # This method shuffles the list.
    def shuffle_list(self) -> List[int]:
        # Shuffling joined list.
        random.shuffle(self.joined_array)
        return self.joined_array
# --- end reused code ---


# 1) This function creates and returns a randomized array of 1000 elements,
# As per question requierment, each being 2, 3, or 4 with roughly the same probability.
def alea() -> List[int]:
    twos   = GenerateArrays.generate_list_of_nums(2, 334)
    threes = GenerateArrays.generate_list_of_nums(3, 333)
    fours  = GenerateArrays.generate_list_of_nums(4, 333)

    # Using ArrayTools to join and shuffle
    tools_1 = ArrayTools(twos, threes)
    first_join = tools_1.join_lists()  

    tools_2 = ArrayTools(first_join, fours)
    full_array = tools_2.join_lists()  
    tools_2.shuffle_list()             

    return tools_2.joined_array        


# 2) Monte Carlo, pick one random index and
#    print output only if the the value is 2.
def pick(a: List[int]) -> None:
    i = random.randrange(len(a))
    if a[i] == 2:
        print(i)

def main():
    arr = alea()
    pick(arr)


if __name__ == "__main__":
    main()
