"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 3 Greedy Algorithm
Task:
    Worksheet Task 02
    
    Run the Egyptian Fractions for the following example 5/121 using the code

    Check it out manually the expected result, which should be:

    5/121 = 1/5 + 1/757 + 1/763 309 + 1/873 960 180 913 + 1/1 527 612 795 642 093 418 846 225

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
    # calling the Egyptian fraction greedy algorithm on 5/121
    egyptian(5, 121) 
    


if __name__ == "__main__":
    main()