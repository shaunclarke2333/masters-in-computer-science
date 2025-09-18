"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 3 Greedy Algorithm
Task:
    Worksheet Task 03
    
    Run the Knapsack Greedy code for the following cases (list of items - [value, weight])

    ([5,10] [8,20] [12,30]) - capacity 838

    ([3,17] [5,23] [7,29] [11,31] [13,37] - capacity 997

    ([5,25] [6,36] [7,49] [8,64]) - capacity 250

    ([5,25] [6,36] [7,49] [8,64]) - capacity 360
"""
from typing import List
# knapsack unbounded - Greedy approach

def knapsack(v, w, cap):
    rwv = []         # triplet ratio, weight, value, index
    for i in range(len(v)):
        rwv.append([v[i]/w[i],w[i],v[i],i])
    rwv.sort(reverse=True)    # sort from high to low rate
    ans = []                     # the list of added items
    tw = 0                                  # total weight
    found = True
    while (found):        # until no fitting item is found
        found = False
        for t in rwv:              # search an item to add
            if (t[1] + tw) <= cap:      # if the item fits
                ans.append(t[3])                  # add it
                tw += t[1]
                found = True
                break
    return ans           # returns the list of added items

def main():
    #([5,10] [8,20] [12,30]) - capacity 838
    values: List = [5, 8, 12]
    weights: List = [10, 20, 30]
    cap: int = 838
    print(knapsack(values, weights, cap))
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # ([3,17] [5,23] [7,29] [11,31] [13,37] - capacity 997
    values: List = [3, 5, 7, 11, 13]
    weights: List = [17, 23, 29, 31, 37]
    cap: int = 997
    print(knapsack(values, weights, cap))
    #[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

    # ([5,25] [6,36] [7,49] [8,64]) - capacity 250
    values: List = [5, 6, 7, 8]
    weights: List = [25, 36, 49, 64]
    cap: int = 250
    print(knapsack(values, weights, cap))
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # ([5,25] [6,36] [7,49] [8,64]) - capacity 360
    values: List = [5, 6, 7, 8]
    weights: List = [25, 36, 49, 64]
    cap: int = 360
    print(knapsack(values, weights, cap))
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # values: List = [2, 4, 5]
    # weights: List = [1, 3, 10]
    # cap: int = 14
    # print(knapsack(values, weights, cap))

if __name__ == "__main__":
    main()

