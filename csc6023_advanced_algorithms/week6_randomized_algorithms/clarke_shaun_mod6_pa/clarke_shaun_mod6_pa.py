
"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 6 Randomized Algorithms
Assignment: 
    Create a program that calls the function myFunction(x) from 0 to 9999 and stores the results in an array. Your program should then apply the Hill Climbing algorithm several times (you can set this up Monte Carlo or Las Vegas style) to find the value of x that delivers the largest value for the function. Each time you call the hill climbing function you will pass in the array and a random starting index, x.

    On each attempt at finding the largest value, the initial search value x is chosen randomly between the values 1 to 9998.

    You can use this function to test your program, but your program should work with any version of myFunction(x).

    image_2022-08-17_081913370.png


    Of course with just 10000 values in the array, we could just use the Python's max(list) to determine the element with the greatest value; for this project, however, we are trying to simulate a situation in which it would not be practical to do that. At the end of your program, whether it is applying a Las Vegas approach or a Monte Carlo approach, it should print a statement saying how many times it attempted the hill climbing algorithm and what the greatest local maximum it found was; it should also list the actual (global) maximum which you can determine with max(list).

    For example: "After ten tries, the greatest local maximum discovered was 17434. The actual global maximum was 25405." or "After 100 tries, the greatest local maximum discovered was 25405 which was the global maximum." 

    If you are using the Monte Carlo style approach, where finding the global maximum is not guaranteed, whether you find the global maximum will be heavily dependent on the amount of peaks and valleys created by the function and the value of k. For the myFunction function provided above, you may have to set k equal to a very high number to reliably get the global maximum, though there it is not required that the global maximum needs to be returned. 

    Your program must include and use a function called "hillClimb(arr, start_index)" that does the following:

    accepts two parameters, an array, arr, and a starting index, start_index). They should be named "arr" and "start_index". (You generate the array using "myFunction" above and you should generate the start_index with a pseudorandom number generator, but you should test this on small examples.)
    returns the index of the local peak and the value in this fashion: return local_maximum_index, arr[local_maximum_index] (Please note that "local_maximum_index" can be called whatever you want but the two returned values need to be arranged in that order above. Do not put them in a list ("[ ]") or other data structure.
    If the starting index is a local peak, the starting index and its value should be returned.
    If the starting index ends up in a pit, with equal increases to the left and to the right, search to the right. This is an arbitrary decision I am forcing upon you based on testing requirements on my end.
    If the starting index ends up in a pit with unequal increases to the left and right, search the higher path.
    Make sure your searching can go all the way to the ends of the array if need be.
    Make sure your program can traverse shoulders. If at the end of the shoulder, the values start to decrease, you should end at the last part of the shoulder. For example hillClimb([6,5,5,5,4,3,2],5) should return the index 0 and the value 6 but hillClimb([2,5,5,5,4,3,2],5) should return the index 1 and the value 5.

"""

from typing import List, Tuple, Optional
import random
from math import log2


# myFunction(x) from the slide 
def myFunction(x):
    if (x == 0):
        return 0
    elif ((log2(x) + 7) % 17) < (x % 13):
        return (x + log2(x))**3
    elif ((log2(x) + 5) % 23) < (x % 19):
        return (log2(x) + 2)**3
    else:
        return (log2(x)**2) - x


# Generate the array 
def build_array(n: int = 10000) -> List[int]:
    """
    Call myFunction(x) for x = 0 to n-1 and store the results.
    """
    arr: List[int] = []
    i: int = 0
    while i < n:
        arr.append(myFunction(i))
        i += 1
    return arr


# Hill clinbing fucntion
def hillClimb(arr: List[int], start_index: int) -> Tuple[int, int]:
    """
    Move uphill until a local maximum or end of a shoulder is reached.
    Returns: (local_max_index, arr[local_max_index])
    """
    n: int = len(arr)
    i: int = start_index
    # This variable will indicate if we are going left or right.
    last_dir: Optional[str] = None  

    # adding some guard rails logic.
    if i < 0:
        i = 0
    if i > n - 1:
        i = n - 1

    while True:
        # either end will be consiodered a peak
        if i == 0 or i == n - 1:
            return i, arr[i]

        cur: int = arr[i]
        left_val: int = arr[i - 1]
        right_val: int = arr[i + 1]

        #local peak
        if left_val < cur and right_val < cur:
            return i, cur

        # handle shoulders
        if left_val == cur or right_val == cur:
            if last_dir == 'left':
                # Go left while equal
                while i > 0 and arr[i - 1] == cur:
                    i -= 1
                # if we dip on the next, stop at the last equal
                if i == 0 or arr[i - 1] < cur:
                    return i, cur
                # if we did npt dip, keep climbing in the main loop
            else:
                # go right when undecided
                while i < n - 1 and arr[i + 1] == cur:
                    i += 1
                if i == n - 1 or arr[i + 1] < cur:
                    return i, cur

        # Handle the dip when both sides higher
        if left_val > cur and right_val > cur:
            inc_left: int = left_val - cur
            inc_right: int = right_val - cur
            if inc_left == inc_right:
                i += 1
                last_dir = 'right'  
            else:
                if inc_left > inc_right:
                    i -= 1
                    last_dir = 'left'
                else:
                    i += 1
                    last_dir = 'right'
            continue

        # When one side is higher
        if left_val > cur and right_val <= cur:
            i -= 1
            last_dir = 'left'
            continue
        if right_val > cur and left_val <= cur:
            i += 1
            last_dir = 'right'
            continue

        # fallback and regroup
        return i, cur


# The monte carlo function 
def run_monte_carlo(arr: List[int], k: int) -> Tuple[int, int, int]:
    """
    Try k random starts in [1, n-2]. Return (tries, best_index, best_value).
    """
    n: int = len(arr)
    tries: int = 0
    best_idx: int = 0
    best_val: int = -10**18

    while tries < k:
        start_index: int = random.randint(1, n - 2)
        local_idx, local_val = hillClimb(arr, start_index)
        if local_val > best_val:
            best_val = local_val
            best_idx = local_idx
        tries += 1

    return tries, best_idx, best_val


# The las vegas function
def run_las_vegas(arr: List[int], max_tries: int) -> Tuple[int, int, int]:
    """
    Try random starts until we hit the global max or reach max_tries.
    """
    n: int = len(arr)
    tries: int = 0
    best_idx: int = 0
    best_val: int = -10**18
    global_max: int = max(arr)

    while tries < max_tries:
        start_index: int = random.randint(1, n - 2)
        local_idx, local_val = hillClimb(arr, start_index)
        if local_val > best_val:
            best_val = local_val
            best_idx = local_idx
        tries += 1
        if local_val == global_max:
            break

    return tries, best_idx, best_val


# Main function where the magic happens
def main() -> None:

    # Set test to true for hill climbing test cases
    test = False
    if test: 
        print('shoulder test 1:', hillClimb( [6,5,-4,3,2,1], 4))  # expect (3, 3)
        print('shoulder test 2:', hillClimb([2,5,5,5,4,3,2], 5))  # expect (1, 5)
        return 0
    
    


    # Using seed to initialize the pseudo-random number generator for different runs.
    # comment this out to make it repeatable
    # random.seed()

    # Generate the array once
    arr: List[int] = build_array(10000)
    global_max: int = max(arr)

    # Prompt user to select a strategy
    print("\nPick a mode:")
    print("  1) Monte Carlo (fixed number of tries)")
    print("  2) Las Vegas  (stop when global max is found or cap reached)")
    user_input: str = input("Enter 1 or 2: ").strip()

    if user_input == "2":
        cap_raw: str = input("Max number of attempts (I think you dhould try 1000): ").strip()
        try:
            cap: int = int(cap_raw)
        except ValueError:
            cap = 1000

        tries, best_idx, best_val = run_las_vegas(arr, cap)
        if best_val == global_max:
            print(f"\nAfter {tries} tries, the greatest local maximum discovered was {best_val}  at index {best_idx} which was the global maximum.")
        else:
            print(f"\nAfter {tries} tries, the greatest local maximum discovered was {best_val} at index {best_idx}. The actual global maximum was {global_max}.")
    else:
        k_raw: str = input("How many random starts? (if i were you i suggest 100): ").strip()
        try:
            k: int = int(k_raw)
        except ValueError:
            k = 100

        tries, best_idx, best_val = run_monte_carlo(arr, k)
        if best_val == global_max:
            print(f"\nAfter {tries} tries, the greatest local maximum discovered was {best_val} at index {best_idx} which was the global maximum.")
        else:
            print(f"\nAfter {tries} tries, the greatest local maximum discovered was {best_val} at index {best_idx}. The actual global maximum was {global_max}.")

    
if __name__ == "__main__":
    main()
