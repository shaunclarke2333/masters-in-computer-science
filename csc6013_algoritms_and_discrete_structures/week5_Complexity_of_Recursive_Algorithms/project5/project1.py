"""
Develop a Python program with a recursive algorithm to calculate the number of digits in the binary expansion/representation of a positive Integer n.
    if n == 1, the answer is 1;
    if n > 1, the answer is 1 plus the number of digits in the binary representation of n//2.
Run your code for the instances: n = 256 and n = 750.
Create the recurrence relation and stopping condition for your algorithm, and compute the Big Oh complexity using either back substitution or the master method.
"""

def binary_digits(n):
    if n == 1:
        return 1
    else:
        return 1 + binary_digits(n // 2)

# Test cases
print("Digits in binary of 256:", binary_digits(256))
print("Digits in binary of 750:", binary_digits(750))

