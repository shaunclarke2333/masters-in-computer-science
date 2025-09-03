"""
Adapt the Binary Search algorithm saw in class to search a given element assuming that the array is not in ascending order, but instead it is sorted
in descending order. Trace your algorithm execution printing:
    at each recursive call, print the subarray from start to end and show the mid element.
    test your algorithm for the arrays:
        A1 = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]   searching for 44;
        A1 = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]   searching for 56;
        A1 = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]   searching for 42;
        A2 = [9, 7, 6, 4, 2, 0, -1, -3, -5, -8, -9]   searching for -1;
        A2 = [9, 7, 6, 4, 2, 0, -1, -3, -5, -8, -9]   searching for -7.
"""
def binSearch(A, start, end, k):
    mid = (end + start) // 2
    print(f"{A[start:end+1]}, mid = {A[mid]}")
    if start > end:
        return None
    elif A[mid] == k:
        return mid
    elif A[mid] < k:
        return binSearch(A, start, mid - 1, k)
    else:
        return binSearch(A, mid + 1, end, k)

A = list(range(10))  # A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
A1 = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]    #searching for 44;
A1 = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]   #searching for 56;
A1 = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]   #searching for 42;
A2 = [9, 7, 6, 4, 2, 0, -1, -3, -5, -8, -9]   #searching for -1;
A2 = [9, 7, 6, 4, 2, 0, -1, -3, -5, -8, -9]   #searching for -7.

A = A2

for i in [-7]:
    print("{} is at index {}".format(i, binSearch(A, 0, len(A) - 1, i)))
