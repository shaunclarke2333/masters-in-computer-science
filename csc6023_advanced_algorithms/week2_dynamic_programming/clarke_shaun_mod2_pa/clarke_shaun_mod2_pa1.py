"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 2 Dynamic Programming
Project Assignment:
    Instructions
    Project #2

        Create a program that computes the "Tribonacci" sequence numbers
        ○Unlike the traditional Fibonacci sequence (a number is the sum of the two previous ones), here a number is the sum of the three previous ones (the initial numbers are 1,1,1)

        The first 9 elements of the sequence are:
        1, 1, 1, 3, 5, 9, 17, 31, 57, …

        ■Your program should asks the user a positive Integer n and the deliver the n-th element of the Tribonacci sequence

        For example, for n = 6, it delivers 9
        Make sure your program uses Dynamic Programming in an efficient way (for example, keeping in memory previously computed elements)
        This program must be your own, do not use someone else’s code
        Any specific questions about it, please bring to the Office hours meeting this Monday or contact me by email
        This is a challenging program to make sure you are mastering your Python programming skills, as well as your asymptotic analysis understanding
        Don’t be shy with your questions
        The program should not crash if the user enters something other than an integer (like a real number or a non-numeric value) 
        The program should end when the user enters an integer less than 1.
"""
from typing import Dict


def fib(n: int) -> int:
    # Dictionary to hold already computed fibs:
    memoi: Dict = {}
    
    # looping through every number from 1 to n. +1 so it is inclusive.
    for i in range(1, n + 1):
        # print(i)
        # defining the base case so the first three numbers are accounted for.
        if i <= 3:
            result = 1
        else:
            # Look up previous computations
            result = memoi[i - 1] + memoi[i - 2] + + memoi[i - 3]
        # Save the computed fib number
        memoi[i] = result
    
    return memoi[n]

print(fib(6))