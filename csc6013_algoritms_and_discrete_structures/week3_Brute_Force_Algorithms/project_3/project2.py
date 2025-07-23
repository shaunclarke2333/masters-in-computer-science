"""
Author: Shaun Clarke
Class: CSC6013
Goal:
Adapt the Bubble Sort algorithm saw in class to stop the outer loop if no swap was made during the last iteration (thus, the array is already sorted).
Trace your algorithm execution printing:
    at each iteration of the outer loop count the number of times two array elements are compared and the number of times two array elements were swapped, plus the current status of the array.
    test your algorithm for the arrays:
        A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
        A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
        A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]
"""

def bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if (a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]