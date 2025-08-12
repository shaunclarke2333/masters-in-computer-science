"""
Develop a Python program with a recursive algorithm to calculate the sum of the squares of the positive Integers 12 + 22 + 32 + … + n2, given the value of n.
    if n == 1, the answer is 1;
    if n > 1, the answer is n2 plus the sum of the squares up to (n-1).
Run your code for the instances: n = 12 and n = 20.
Create the recurrence relation and stopping condition for your algorithm, and compute the Big Oh complexity using either back substitution or the master method.
"""

def sum_of_squares(n):
    if n == 1:
        return 1
    else:
        return n**2 + sum_of_squares(n - 1)

# Test cases
print("Sum of squares up to 12:", sum_of_squares(12)) 
print("Sum of squares up to 20:", sum_of_squares(20))
