
"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 5 Linear Programming
Assignment: Simple LP helper (matches slides).

Notes:
- No list comprehensions.
- Type hints added.
- Straightforward loops and prints.
"""

from typing import List
import numpy as np


class InputTools:
    @staticmethod
    def parse_floats_list(raw: str, expected_len: int) -> List[float]:
        """
        Handles a comma or space separated list of numbers.
        Ensures the user entered the expected length.
        """
        # Removing brackets in case the user decides to paste an input like [1,2,3]
        cleaned: str = raw.replace('[', '').replace(']', '').replace(';', ',')
        # Split on commas or spaces
        temp: List[str] = cleaned.replace(',', ' ').split()

        parts: List[str] = []
        for item in temp:
            if item.strip() != "":
                parts.append(item)

        nums: List[float] = []
        for p in parts:
            try:
                nums.append(float(p))
            except ValueError:
                raise ValueError("Resistance is futile, all entries must be numbers.\n")

        if len(nums) != expected_len:
            raise ValueError(f"Expected {expected_len} numbers but got {len(nums)}.\nI find your lack of faith disturbing.\n")
        return nums

    @staticmethod
    def ask_int(prompt: str) -> int:
        while True:
            try:
                val: int = int(input(prompt))
                return val
            except ValueError:
                print("You must enter a whole number. Try again young padawan.\n")

    @staticmethod
    def ask_vector(prompt: str, n: int) -> np.ndarray:
        while True:
            try:
                raw: str = input(prompt)
                nums: List[float] = InputTools.parse_floats_list(raw, n)
                return np.array(nums, dtype=float)
            except ValueError as e:
                print(str(e) + ". There is no escape. Don't make me destroy you.\nLets try again comma or space separated entries.\n")

    @staticmethod
    def ask_matrix(n: int) -> np.ndarray:
        """
        Ask for an n x n matrix one row at a time. Each row must have n numbers.
        """
        rows: List[List[float]] = []
        print(f"Enter matrix A as {n} rows (each row has {n} numbers).\n")
        i: int = 0
        while i < n:
            try:
                raw: str = input(f"A row {i + 1}: ")
                row: List[float] = InputTools.parse_floats_list(raw, n)
                rows.append(row)
                i += 1
            except ValueError as e:
                print(str(e) + " The Emperor is not as forgiving as I am, so Please enter that row again.\n")
        return np.array(rows, dtype=float)


class LinearProgSolver:
    def __init__(self, c: np.ndarray, A: np.ndarray, b: np.ndarray) -> None:
        self.c: np.ndarray = c  # objective weights
        self.A: np.ndarray = A  # constraints as a square matrix 
        self.b: np.ndarray = b  # limits vector

        n: int = len(c)
        if A.shape != (n, n):
            raise ValueError("A must be square nxn with n being len(c).")
        if b.shape != (n, ):
            raise ValueError("b must have length n.")

    def single_var_solution(self, i: int) -> np.ndarray:
        """
        Best feasible solution where only variable i is used and the others are set to 0).
        Basically, crank it until we hear the sirens, then you will know what the limit its :).
        """
        col: np.ndarray = self.A[:, i]

        ratios: List[float] = []
        j: int = 0
        while j < len(col):
            if col[j] > 0:
                ratios.append(float(self.b[j] / col[j]))
            j += 1

        if len(ratios) > 0:
            cap: float = min(ratios)
        else:
            cap = 0.0

        x: np.ndarray = np.zeros_like(self.c, dtype=float)
        x[i] = cap
        return x

    def balanced_solution(self) -> np.ndarray:
        """
        Solving Ax = b using explicit inversion + dot product like the pdf from class).
        """
        invA: np.ndarray = np.linalg.inv(self.A)
        x: np.ndarray = invA.dot(self.b)
        return x

    def value(self, x: np.ndarray) -> float:
        return float(np.dot(self.c, x))

    def summary(self) -> None:
        n: int = len(self.c)
        print(f"Objective weights (c): {self.c}")
        print(f"Matrix A:\n{self.A}")
        print(f"Vector b: {self.b}")

        # Solo solutions
        print(f"\n-- Solo (one variable at a time) --")
        solo_indices: List[int] = []
        solo_vectors: List[np.ndarray] = []
        solo_values: List[float] = []

        i: int = 0
        while i < n:
            number_of_item: np.ndarray = self.single_var_solution(i)
            val: float = self.value(number_of_item)

            solo_indices.append(i)
            solo_vectors.append(number_of_item)
            solo_values.append(val)

            print(f"Only var x{i + 1}: x = {number_of_item},  f(x) = {round(val, 6)}")
            i += 1

        # Balanced solution
        print(f"\nBalanced Options:")
        try:
            x_bal: np.ndarray = self.balanced_solution()
            val_bal: float = self.value(x_bal)
            print(f"Balanced x = {0},  f(x) = {1}".format(x_bal, round(val_bal, 6)))
            balanced_ok: bool = True
        except np.linalg.LinAlgError:
            x_bal = None  
            val_bal = float('-inf')
            print(f"Balanced solution: matrix A is singular.")
            balanced_ok = False

        # Deciding best 
        best_label: str = ""
        best_x: np.ndarray | None = None
        best_val: float = float('-inf')

        # Checking solo results first
        k: int = 0
        while k < len(solo_indices):
            if solo_values[k] > best_val:
                best_val = solo_values[k]
                best_x = solo_vectors[k]
                best_label = "Solo variable x{0}".format(solo_indices[k] + 1)
            k += 1

        # Comparing balanced if available
        if balanced_ok and val_bal > best_val:
            best_val = val_bal
            best_x = x_bal 
            best_label = "Balanced"

        print("\n== Best Option ==")
        print(f"{best_label} is best: x = {best_x},  f(x) = {round(best_val, 6)}")


def main() -> None:
   
    # Asking for n and all inputs
    n: int = InputTools.ask_int("Enter number of variables/constraints (n): ")
    c: np.ndarray = InputTools.ask_vector("Enter {0} objective weights c (comma or space separated): ".format(n), n)
    A: np.ndarray = InputTools.ask_matrix(n)
    b: np.ndarray = InputTools.ask_vector("Enter b vector with {0} numbers: ".format(n), n)

    # Solving and summarizing
    solver: LinearProgSolver = LinearProgSolver(c, A, b)
    solver.summary()


if __name__ == "__main__":
    main()
