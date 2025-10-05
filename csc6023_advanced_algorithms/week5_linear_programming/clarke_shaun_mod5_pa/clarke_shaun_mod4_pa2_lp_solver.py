
"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 5 Linear Programming
Assignment: 
    Implement a Linear Programming solver as described in the slides.

    Your program will receive the necessary information for an LP problem namely:

    ○The number of variables (that will be equal to the number of constraint coefficients)

    ■ x

    ○The coefficient of each variable for the objective function (the column profit for slide 13 table)

    ■ f(x)

    ○The data for the square matrix stating the constraint (the inner elements of slide 13 table)

    ■ A

    ○The constraint limits (the last row of slide 13 table)

    ■ b


    Having all input parameters, you will need to compute the possible solution for each variable alone and the solution of the linear equation system Ax = b


    ○To solve the linear equation system you should use the numpy package (further explanation hereLinks to an external site.)


    ■ You will need to import numpy and use the functions:


    array(...) to create a numpy array
    linalg.inv(...) to perform a matrix inversion
    linalg.dot(...) to perform a dot product

    ○For example, the input for slide 13 example can be:


    ○3 variables/constraints, [3,2,2] as weights for the objective function, A = [[2,4,5],[1,2,4],[8,0,3]], and b = [300,200,300]

    For example, the Input for slide 13 example would be:
    ○3 variables/constraints, [3,2,2] as weights for the objective function, A = [[2,4,5],[1,2,4],[8,0,3]], and b = [300,200,300]

    For this example, the call of linear equation system solution can be:
    image_2022-08-10_072752785.png

    Special Requirement: You must include a copy and pasted run of your program (including both the input and output) using one of the test cases from class (either pants/jackets or the chemicals) or both. This will be worth a portion of the grade and helps greatly in testing the projects. 

    The output should be the Real number of unit to each of the variables


"""

# importing dependencies
from typing import List
import numpy as np


class InputTools:

    @staticmethod
    def parse_floats_list(user_input: str, expected_len: int) -> List[float]:
        """
        Handles a comma or space separated list of numbers.
        Ensures the user entered the expected length.

        """
        # Removing brackets in case the user decides to paste an input like [1,2,3]
        cleaned: str = user_input.replace('[', '').replace(']', '').replace(';', ',')
        # Split on commas or spaces 
        temp: List[str] = cleaned.replace(',', ' ').split()

        # Keep only parts that are not emopty
        parts: List[str] = []
        for item in temp:
            if item.strip() != "":
                parts.append(item)

        # Convert each str to float
        nums: List[float] = []
        for p in parts:
            try:
                nums.append(float(p))
            except ValueError:
                raise ValueError("Resistance is futile, all entries must be numbers.\n")

        # Mkaing sure we get the expected count
        if len(nums) != expected_len:
            raise ValueError(f"Expected {expected_len} numbers but got {len(nums)}.\nI find your lack of faith disturbing.\n")
        return nums

    @staticmethod
    def ask_int(prompt: str) -> int:
        """
        This static method prompts the user for input until the required input is entered
        """
        while True:
            try:
                # Prompting user for input and converting it to int
                val: int = int(input(prompt))   
                return val                      
            except ValueError:
                print("You must enter a whole number. Try again young padawan.\n")

    @staticmethod
    def ask_vector(prompt: str, n: int) -> np.ndarray:
        """
        This static method prompts the user for a vector of length n and return it as a numpy 1-D float array.

        """
        while True:
            try:
                # Prompts the user for input
                user_input: str = input(prompt)
                # Split user input into a list and convert the strings to floats                     
                nums: List[float] = InputTools.parse_floats_list(user_input, n)
                # Convert the list of floats to a numpy array  
                return np.array(nums, dtype=float)           
            except ValueError as e:
                print(f"There is no escape. Don't make me destroy you.\nLets try again comma or space separated entries.\n")

    @staticmethod
    def ask_matrix(n: int) -> np.ndarray:
        """
        Ask for an n x n matrix one row at a time. Each row must have n numbers.

        """
        # Empty list to hold each row
        rows: List[List[float]] = []               
        print(f"Enter matrix A as {n} rows (each row has {n} numbers).\n")
        i: int = 0
        # While loop to collect exactly n rows
        while i < n:
            try:
                # prompt user for input with row counter
                user_input: str = input(f"A row {i + 1}: ")
                # Call parse floats to split and convert inputs to float            
                row: List[float] = InputTools.parse_floats_list(user_input, n)
                # adding each converted row to rows  
                rows.append(row)
                # Move tot he next row 
                i += 1                                            
            except ValueError as e:
                print(str(e) + " The Emperor is not as forgiving as I am, so Please enter that row again.\n")
        # Rerurning list of lists that was converted to a 2 D numpy array
        return np.array(rows, dtype=float)         


class LinearProgSolver:

    def __init__(self, c: np.ndarray, A: np.ndarray, b: np.ndarray) -> None:
       
        self.c: np.ndarray = c  # objective weights 
        self.A: np.ndarray = A  # constraints as a square matrix 
        self.b: np.ndarray = b  # limits vector

        n: int = len(c) # number of variables/constraints
        if A.shape != (n, n):  # making sure A is square nxn
            raise ValueError("A must be square nxn with n being len(c).")
        if b.shape != (n, ): # making sure b has length n
            raise ValueError("b must have length n.")

    def single_var_solution(self, i: int) -> np.ndarray:
        """
        Compute the best feasible solution where only variable i is used and everything else is set to 0.
        Basically, crank it until we hear the sirens, then you will know what the limit is :).

        """
        # coefficients for variable i across the rules
        col: np.ndarray = self.A[:, i]
        # list of allowed max values for var i from each rule
        ratios: List[float] = []                
        j: int = 0
        while j < len(col):
            # logic for rows where A[j,i] > 0
            if col[j] > 0:                      
                ratios.append(float(self.b[j] / col[j]))
            j += 1

        # Making sure we get the best limit, otherwise cap it at 0
        if len(ratios) > 0:
            cap: float = min(ratios)
        else:
            cap = 0.0

        # Creating the solution vector with all zeros except position i
        x: np.ndarray = np.zeros_like(self.c, dtype=float)
        x[i] = cap
        return x

    def balanced_solution(self) -> np.ndarray:
        """
        Solving the system A x = b for x using matrix inversion and dot product like we went over in the class PDF. 

        """
        # linalg.inv(...) to perform a matrix inversion
        invA: np.ndarray = np.linalg.inv(self.A)
        # linalg.dot(...) to perform a dot product   
        x: np.ndarray = invA.dot(self.b)           
        return x

    def value(self, x: np.ndarray) -> float:
        """
        This method multiplies matching entries of c and x, then add them up

        """
        return float(np.dot(self.c, x))

    def summary(self) -> None:
        """
        This method kee[s things clean by doing all the work here for a clean output:
        
        """
        n: int = len(self.c)
        print(f"Objective weights (c): {self.c}")
        print(f"Matrix A:\n{self.A}")
        print(f"Vector b: {self.b}")

        # Single solutions
        print(f"\n-- single (one variable at a time) --")
        # Lists to hold the following: singled variable, x vector for that variable and the dot product of x times x
        single_indices: List[int] = []         
        single_vectors: List[np.ndarray] = []  
        single_values: List[float] = []        

        i: int = 0
        while i < n:
            #Computing the single vector for var i
            number_of_item: np.ndarray = self.single_var_solution(i)
            # The objective value  
            val: float = self.value(number_of_item)             

            single_indices.append(i)
            single_vectors.append(number_of_item)
            single_values.append(val)

            print(f"Only var x{i + 1}: x = {number_of_item},  f(x) = {round(val, 6)}")
            i += 1

        # Balanced solution 
        print(f"\nBalanced Options:")
        try:
            x_bal: np.ndarray = self.balanced_solution()       
            val_bal: float = self.value(x_bal)
            print(f"Balanced x = {x_bal},  f(x) = {round(val_bal, 6)}")
            balanced_exists: bool = True
        except np.linalg.LinAlgError:
            # mark unbalanced solution
            x_bal = None                                       
            val_bal = float('-inf')                           
            print(f"Balanced solution: matrix A is singular.")
            balanced_exists = False

        # Decide which outcome is best by its value
        # Label to print at the end
        best_label: str = ""                 
        # corresponding x vector
        best_x: np.ndarray | None = None     
        # tracking the highest value and using -inf to ensure the best value is picked 
        best_val: float = float('-inf')      

        # Checking all single results
        k: int = 0
        while k < len(single_indices):
            if single_values[k] > best_val:
                best_val = single_values[k]
                best_x = single_vectors[k]
                best_label = "single variable x{0}".format(single_indices[k] + 1)
            k += 1

        # Comparing balanced against the best we got so far if it exists
        if balanced_exists and val_bal > best_val:
            best_val = val_bal
            best_x = x_bal 
            best_label = "Balanced"

        print("\nBest Option")
        print(f"{best_label} is best: x = {best_x},  f(x) = {round(best_val, 6)}")


def main() -> None:
    """
    This method is where the magic happensd
    """
    # Asking user for all inputs
    n: int = InputTools.ask_int("Enter number of variables/constraints (n): ")
    c: np.ndarray = InputTools.ask_vector("Enter {0} objective weights c (comma or space separated): ".format(n), n)
    A: np.ndarray = InputTools.ask_matrix(n)
    b: np.ndarray = InputTools.ask_vector("Enter b vector with {0} numbers: ".format(n), n)

    # Calling LinearProgSolver to solve and asummarize.
    solver: LinearProgSolver = LinearProgSolver(c, A, b)
    solver.summary()


if __name__ == "__main__":
    main()

# How to run this program
# Enter number of variables/constraints (n): 2
# Enter 2 objective weights c (comma or space separated): 50 40
# Enter matrix A as 2 rows (each row has 2 numbers).
# A row 1: 2 3
# A row 2: 2 1
# Enter b vector with 2 numbers: 1500 1000
