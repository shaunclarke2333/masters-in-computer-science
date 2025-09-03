from typing import List

"""
Adapt the Maximum Element in an Array algorithm saw in class to search for the minimum element in the array.
Trace your algorithm execution printing:
    at the beginning of each recursive call the start and end values.
    at the returning of each recursive call the returned value (the minimum of the array slice).
    test your algorithm for the arrays:
        A3 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
        A4 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
        A5 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]
"""

def Min(A, start, end):
    # At the beginning of each recursive call the start and end values.
    print(f"Start: {start}, End: {end}")
    if start == end:
        return end
    else:
        mid = (end + start) // 2
        fst = Min(A, start, mid)
        lst = Min(A, mid + 1, end)
        number = fst if A[fst] < A[lst] else lst
        # At the returning of each recursive call the returned value (the minimum of the array slice).
        print(f"Returning: {A[number]}")
        return number
    
A3 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
A4 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
A5 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]

A = A5

i = Min(A, 0, len(A) - 1)
print("The minimum number is", A[i], "at index", i)

