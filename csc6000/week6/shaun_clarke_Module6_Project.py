"""
Check Inverse Matrices
Write a Python program that receives two matrices to check if they are inverse one to each other.
Your program should then verify if the two matrices are the inverse of the other:
  Multiply the matrices to confirm:
    If the matrices cannot be multiplied, then they are not inverses to each other;
    If their multiplication does not give an Identity matrix, they are not inverses to each other.
Pay attention to the fact that working with Real numbers, thus using floating point representation to perform arithmetic operations, you should expect errors in decimal places. 
Therefore, always round your obtained results with a reasonable number of decimal places using the Python's built-in function round(x, d) that rounds up the content of variable x with d decimal digits.
For example, if x = 0.99999999996 is round by round(x, 5) the result will be 1.00000.

"""

"""
how to check if two matrices are inverse of each other
To check if two square matrices are inverses of each other, you need to perform matrix multiplication. 
Here's the process:
1. Understanding Matrix Inverse:
Two matrices, A and B, are inverses of each other if their product (in both orders) results in the identity matrix (I).
The identity matrix (I) is a square matrix with ones along the main diagonal and zeros everywhere else.
Mathematically, this means: A * B = B * A = I. 
2. Steps to Check:
Ensure Matrices are Square: Both matrices must be square and have the same dimensions (e.g., both 2x2, both 3x3). 
Perform Matrix Multiplication:
Multiply matrix A by matrix B (A * B).
Multiply matrix B by matrix A (B * A). 
Check for Identity Matrix:
If both A * B and B * A result in the identity matrix (I), then the matrices are inverses of each other.
If either product does not equal the identity matrix, then they are not inverses. 
"""