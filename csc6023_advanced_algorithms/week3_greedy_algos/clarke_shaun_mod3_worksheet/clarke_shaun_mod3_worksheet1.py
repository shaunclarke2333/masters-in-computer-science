"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 3 Greedy Algorithm
Task:
    Worksheet Task 01
    
    Run the Egyptian Fractions for the following examples:

    5/6, 7/15, 23/34, 121/321, 5/123

    Write remarks in your new code with the solution of such cases
    
"""
# Egyptian Fraction Greedy 
from math import ceil
from typing import List

# n is the numerator, d is the denominator
def egyptian(n: int, d: int) -> str:
    
    print("The Egyptian Fraction of {}/{}".format(n, d))
    ans: List = []
    # while numerator is not 0
    while (n > 0):
        x: int = ceil(d / n)    # compute the minimal larger denominator
        ans.append(x)           # add it to the numerator list
        n, d = x * n - d, d * x # update the remainder to n and d
    for a in ans:
        print("\n1/{}".format(a), end=" ")

def main():
    # calling the Egyptian fraction greedy algorithm on 5/6, 7/15, 23/34, 121/321, 5/123
    egyptian(5, 6) # 1/2 1/3
    print("")
    egyptian(7, 15) # 1/3 1/8 1/120
    print("")
    egyptian(23, 34) # 1/2 1/6 1/102
    print("")
    egyptian(121, 321)# 1/3 1/23 1/7383
    print("")
    egyptian(5, 123)# 1/25 1/1538 1/4729350


if __name__ == "__main__":
    main()