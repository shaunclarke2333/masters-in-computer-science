"""
Develop one Python program to perform the Quicksort, but instead of sorting the elements in ascending order (from the smallest to the largest),
the elements are sorted in the decrescent order (from the larger to the smallest).

Your program also have to compute and print at the end the number of swaps performed and the number of recursive calls.

Test your program over the following arrays:

A = [38, 21, 39, 60, -1, 10, 81, 23]
B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]

You have to submit the code (.py file) of your algorithm, plus the .pdf of the trace for the three required tests.
It is expected that your code performs the computations necessary for the traces (count the number of calls and swaps).


"""
from typing import List

# Counters for swaps and recursive calls
swap_counter = 0
recursive_counter = 0

def lomuto(A: List, left: int, right: int) -> int:
    global swap_counter
    p: int = A[right]
    i: int = left
    
    for j in range(left, right):
        if A[j] > p:
            swap_counter += 1
            A[i], A[j] = A[j], A[i]
            i += 1
    swap_counter += 1
    A[i], A[right] = A[right], A[i]
    return i

def quicksort(A: List[int], left: int, right: int) -> List:
    global recursive_counter
    if (left < right):
        mid = lomuto(A, left, right)
        
        recursive_counter += 1
        quicksort(A, left, mid-1)
        recursive_counter += 1
        quicksort(A, mid+1, right)
    return A

A = [38, 21, 39, 60, -1, 10, 81, 23]
B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
an_aray = C 
print(f"Sorted Array: {quicksort(an_aray, 0, len(an_aray)-1)}\nTotal swaps: {swap_counter}\nTotal recursive call: {recursive_counter}")