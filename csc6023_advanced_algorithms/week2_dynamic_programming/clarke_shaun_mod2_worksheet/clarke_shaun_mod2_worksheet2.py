"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 2 Dynamic Programming
Task:
    Worksheet Task 02
    Implement a recursive program that asks the number of disks and delivers the minimal number of moves to solve the Towers of Hanoi efficiently
    Your program must have a recursive function that delivers the number of movements for a given number of disks; it does NOT need to give the moves themselves.
    
"""

def moves(num_disks: int) -> int:
    # print(f"T(n) = 2^n - 1")

    base: int = 2
    # any number raised to the power of 0 is 1.
    if num_disks == 0:
        return 1
    # if the number entred is 1 then we return 2 which is the base we are working with.
    elif num_disks == 1:
        return base
    # For any number that is not 0 or 1, multiply base by the output of moves
    else:
        return base * moves(num_disks - 1)
    



print(moves(0)-1)