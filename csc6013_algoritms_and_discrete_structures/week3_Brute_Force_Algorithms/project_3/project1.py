"""
Author: Shaun Clarke
Class: CSC6013
Adapt the Selection Sort algorithm saw in class to sort the elements being the largest ones selected to go to the last positions first
instead of the version presented in class, where the smallest ones where selected to go to the first positions. Trace your algorithm execution printing:
    at each iteration of the outer loop count the number of times two array elements are compared and
    the number of times two array elements were swapped, plus the current status of the array.

    test your algorithm for the arrays:
        A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
        A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
        A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]
"""

def selection_sort(a):
    for i in range(len(a)-1):
        min_index = i
        for j in range(i+1, len(a)):
            if (a[j] < a[min_index]):
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]