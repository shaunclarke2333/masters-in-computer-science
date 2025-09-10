"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 2 Dynamic Programming
Task:
    Worksheet Task 01
    
"""


# balanced 0-1 matrices

from itertools import combinations

def permutations(n):
    ones = list(combinations(list(range(n)),n//2))
    ans = []
    for o in ones:
        case = []
        for i in range(n):
            if (i in o):
                case.append(1)
            else:
                case.append(0)
        ans.append(case)
    return ans

def check(mat):
    n = len(mat[0])
    for j in range(n):
        acc0, acc1 = 0, 0
        for i in range(len(mat)):
            if (mat[i][j] == 1):
                acc1 += 1
            elif (mat[i][j] == 0):
                acc0 += 1
            if (acc0 > (n//2)) or (acc1 > n//2):
                return False
    return True

def layer(r, mat, perm, ans):
    for p in perm:
        mat.append(p)
        if check(mat):
            if (r+1 == len(p)):
                ans += 1
            else:
                ans = layer(r+1, mat, perm, ans)
        mat.pop()
    return ans

def balanced01mat():
    matrices = [2,4,6]

    for m in matrices:
        if m == 2:
            print(f"Computing the number of balanced matrices for {m}")
            n = m
            while ((n % 2) == 1) or (n < 0):
                n = int(input("Enter an even matrix order:"))
            perm2 = permutations(n)
            ans2 = layer(0, [], perm2, 0)# 2
            print("The number of balanced matrices is", ans2)
        elif m == 4:
            print(f"Computing the number of balanced matrices for {m}")
            n = m
            while ((n % 2) == 1) or (n < 0):
                n = int(input("Enter an even matrix order:"))
            perm4 = permutations(n)
            ans4 = layer(0, [], perm4, 0)# 90
            print("The number of balanced matrices is", ans4)
        elif m == 6:
            print(f"Computing the number of balanced matrices for {m}")
            n = m
            while ((n % 2) == 1) or (n < 0):
                n = int(input("Enter an even matrix order:"))
            perm6= permutations(n)
            ans6 = layer(0, [], perm6, 0)# 297200
            print("The number of balanced matrices is", ans6)
    

balanced01mat()
