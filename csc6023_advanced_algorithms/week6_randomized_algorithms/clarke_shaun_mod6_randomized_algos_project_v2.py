
"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 6 Randomized Algorithms
Assignment: Week 6 Project – Hill Climbing (Monte Carlo / Las Vegas)

Notes:
- Keep it simple: loops, clear prints, light comments.
- hillClimb(arr, start_index) follows the rules in the prompt.
- Works with any myFunction(x). I put a test version here that matches the slide image.
"""

from typing import List, Tuple, Optional
import random
import math


# ---------------- myFunction(x) from the slide image (test version) ----------------
def myFunction(x: int) -> int:
    """
    Test version based on the screenshot. Use any myFunction(x) when grading.
    """
    if x == 0:
        return 0
    # precompute once
    lg = math.log2(x)

    # branch 1
    if ((lg + 7) % 17) < (x % 13):
        return int(round((x + lg) ** 3))
    # branch 2
    elif ((lg + 5) % 23) < (x % 19):
        return int(round((lg + 2) ** 3))
    # else branch
    else:
        return int(round((lg ** 2) - x))


# ---------------- build the array ----------------
def build_array(n: int = 10000) -> List[int]:
    """
    Call myFunction(x) for x = 0..n-1 and store the results.
    """
    arr: List[int] = []
    i: int = 0
    while i < n:
        arr.append(myFunction(i))
        i += 1
    return arr


# ---------------- hill climbing per rubric ----------------
def hillClimb(arr: List[int], start_index: int) -> Tuple[int, int]:
    """
    Move uphill until a local maximum (or end of a plateau) is reached.

    Returns: (local_max_index, arr[local_max_index])
    """
    n: int = len(arr)
    i: int = start_index
    last_dir: Optional[str] = None  # 'left' or 'right'

    # safety clamp
    if i < 0:
        i = 0
    if i > n - 1:
        i = n - 1

    while True:
        # ends are peaks from this algorithm's POV
        if i == 0 or i == n - 1:
            return i, arr[i]

        cur: int = arr[i]
        left_val: int = arr[i - 1]
        right_val: int = arr[i + 1]

        # strict local peak
        if left_val < cur and right_val < cur:
            return i, cur

        # handle plateaus (shoulders)
        if left_val == cur or right_val == cur:
            if last_dir == 'left':
                # walk left while equal
                while i > 0 and arr[i - 1] == cur:
                    i -= 1
                # if it drops next, stop at the last equal
                if i == 0 or arr[i - 1] < cur:
                    return i, cur
                # else it rises, keep climbing in the main loop
            else:
                # default go right when undecided
                while i < n - 1 and arr[i + 1] == cur:
                    i += 1
                if i == n - 1 or arr[i + 1] < cur:
                    return i, cur
            # continue to main decisions

        # pit: both sides higher
        if left_val > cur and right_val > cur:
            inc_left: int = left_val - cur
            inc_right: int = right_val - cur
            if inc_left == inc_right:
                i += 1
                last_dir = 'right'  # equal -> right
            else:
                if inc_left > inc_right:
                    i -= 1
                    last_dir = 'left'
                else:
                    i += 1
                    last_dir = 'right'
            continue

        # one side higher
        if left_val > cur and right_val <= cur:
            i -= 1
            last_dir = 'left'
            continue
        if right_val > cur and left_val <= cur:
            i += 1
            last_dir = 'right'
            continue

        # fallback
        return i, cur


# ---------------- runners ----------------
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


def run_las_vegas(arr: List[int], max_tries: int) -> Tuple[int, int, int]:
    """
    Try random starts until we hit the global max or reach max_tries.
    Return (tries, best_index, best_value).
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


# ---------------- main ----------------
def main() -> None:
    print("CSC6023 - Week 6 - Randomized Algorithms - Hill Climbing Project\n")

    # seed for different runs; comment this out to make it repeatable
    random.seed()

    # build the array once
    print("Building myFunction(x) array for x = 0..9999...")
    arr: List[int] = build_array(10000)
    global_max: int = max(arr)

    # choose strategy
    print("\nPick a mode:")
    print("  1) Monte Carlo (fixed number of tries)")
    print("  2) Las Vegas  (stop when global max is found or cap reached)")
    choice: str = input("Enter 1 or 2: ").strip()

    if choice == "2":
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

    # quick shoulder tests (from prompt) – uncomment to verify
    # print('shoulder test 1:', hillClimb([6,5,5,5,4,3,2], 5))  # expect (0, 6)
    # print('shoulder test 2:', hillClimb([2,5,5,5,4,3,2], 5))  # expect (1, 5)


if __name__ == "__main__":
    main()
