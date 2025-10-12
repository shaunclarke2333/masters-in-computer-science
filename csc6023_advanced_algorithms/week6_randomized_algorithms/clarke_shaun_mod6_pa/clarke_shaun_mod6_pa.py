
"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 6 Randomized Algorithms
Assignment: Week 6 Project Hill Climbing (Monte Carlo / Las Vegas)



"""

from typing import List, Tuple, Optional
import random
from math import log2


#myFunction(x) from the slide 
def myFunction(x):
    if (x == 0):
        return 0
    elif ((log2(x) + 7) % 17) < (x % 13):
        return (x + log2(x))**3
    elif ((log2(x) + 5) % 23) < (x % 19):
        return (log2(x) + 2)**3
    else:
        return (log2(x)**2) - x


#Generate the array 
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


#Hill clinbing fucntion
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
    
    


    # seed for different runs; comment this out to make it repeatable
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
        cap_raw: str = input("Max number of attempts (suggest 1000): ").strip()
        try:
            cap: int = int(cap_raw)
        except ValueError:
            cap = 1000

        tries, best_idx, best_val = run_las_vegas(arr, cap)
        if best_val == global_max:
            print(f"\nAfter {tries} tries, the greatest local maximum discovered was {best_val} which was the global maximum.")
        else:
            print(f"\nAfter {tries} tries, the greatest local maximum discovered was {best_val}. The actual global maximum was {global_max}.")
    else:
        k_raw: str = input("How many random starts? (suggest 100): ").strip()
        try:
            k: int = int(k_raw)
        except ValueError:
            k = 100

        tries, best_idx, best_val = run_monte_carlo(arr, k)
        if best_val == global_max:
            print(f"\nAfter {tries} tries, the greatest local maximum discovered was {best_val} which was the global maximum.")
        else:
            print(f"\nAfter {tries} tries, the greatest local maximum discovered was {best_val}. The actual global maximum was {global_max}.")

    
if __name__ == "__main__":
    main()
