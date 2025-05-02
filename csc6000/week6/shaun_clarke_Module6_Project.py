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





# This function takes in 2 matrices and multiplies them and returns the product.
def matrices_multi(A,B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            tmp = 0
            for k in range(len(B)):
                tmp += A[i][k] * B[k][j]
            C[-1].append(round(tmp,5))
    print(f" The matrices product is: {C}", end="\n\n")
    return C

# This function takes in the output product of 2 matrices and checks the identity
def verify_identity(matrices_product):
    # looping through each row which is the number of lists in the matrices product list
    for row in range(len(matrices_product)):
        # print(f" This is row {row}")
        # Looping through each column inside the first row for the range of the columns
        for column in range(len(matrices_product[0])):
            print(f" This is row {row},column {column}", end="\n\n")
            # we are on the diagonal but the value is not 1 not inverse
            if row == column and matrices_product[row][column] != 1:
                print(f"The matrices you entered are not inverses to each other\n{matrices_product}", end="\n\n")
                return False
            # if we are off the diagonal and the value is not 0 not inverse
            elif row != column and matrices_product[row][column] != 0:
                print(f"The matrices you entered are not inverse to each other\n{matrices_product}", end="\n\n")
                return False
    print(f"The matrices you entered are inverse to each other\n{matrices_product}", end="\n\n")
    return True


# Checking if the matrices are inverse to each other
def is_inverse(A,B):
    # Getting product of matrices
    matrices_product = matrices_multi(A,B)

    # verifying if the product of the matrices are inverse to each other
    verify_identity(matrices_product)

A = [[1,2,3],[0,1,4],[5,6,0]]
B = [[-24,18,5],[20,-15,-4],[-5,4,1]]

is_inverse(A,B)