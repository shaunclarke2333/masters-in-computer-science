"""
Title: PROJECT 3
Author: Shaun Clarke
Goal:
3) Given an integer n>=2 and two nxn matrices A and B of real numbers,
find the product AB of the matrices.
Your function should have three input parameters –
a positive integer n and two nxn matrices of numbers– and
should return the nxn product matrix using a return statement.
"""

# importing dependencies
from typing import List

# This class finds the product of 2 matrices
class MatricesProduct:
    
    # This method takes in 2 matrices and multiplies them and returns the product.
    @staticmethod
    def matrices_multi(n: int, A: List, B: List):
        C: List = []
        # looping through number of matrix dimensions
        for i in range(n):
            C.append([])
            for j in range(n):
                tmp: int = 0
                for k in range(n):
                    tmp += A[i][k] * B[k][j]
                C[-1].append(round(tmp,5))
        
        return C

# This function calls the program
def main():
    
    # initializing input parameters
    n = 2
    A = [[2, 7], [3, 5]]
    B = [[8, -4], [6, 6]]
    
    # calculating the matrices product
    output = MatricesProduct.matrices_multi(n,A,B)
    
    # formatting output for printing
    print(f" The matrices product is: {output}", end="\n\n")

# Running program if script is invoked directly 
if __name__ == "__main__":
    main()
