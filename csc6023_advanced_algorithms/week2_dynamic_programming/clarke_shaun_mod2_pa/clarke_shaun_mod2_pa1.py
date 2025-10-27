text = """
Uncomment this 
*********IN A CSC6023 CLASS FAR FAR AWAY*********
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 2 Dynamic Programming
Project Assignment:
    Instructions
    Project #2

        Create a program that computes the "Tribonacci" sequence numbers
        ○Unlike the traditional Fibonacci sequence (a number is the sum of the two previous ones),
        here a number is the sum of the three previous ones (the initial numbers are 1,1,1)

        The first 9 elements of the sequence are:
        1, 1, 1, 3, 5, 9, 17, 31, 57, …

        ■Your program should asks the user a positive Integer n and the deliver the n-th element of the Tribonacci sequence

        For example, for n = 6, it delivers 9
        Make sure your program uses Dynamic Programming in an efficient way (for example, keeping in memory previously computed elements)
        This program must be your own, do not use someone else’s code
        Any specific questions about it, please bring to the Office hours meeting this Monday or contact me by email
        This is a challenging program to make sure you are mastering your Python programming skills, 
        as well as your asymptotic analysis understanding
        Don’t be shy with your questions
        The program should not crash if the user enters something other than an integer (like a real number or a non-numeric value) 
        The program should end when the user enters an integer less than 1.
        <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> <o> 
"""
from typing import Dict
import os, time, shutil, textwrap


class DoTheFib:
    def __init__(self, n):
        self.n = n

    def calculate_fib(self) -> int:
        """
        This method asks the user for a positive Integer n and the delivers the n-th element of the Tribonacci sequence
        """
        # Dictionary to hold already computed fibs:
        memoi: Dict = {}

        n = self.n

        # If n is less than 1, exit the program
        if n < 1:
            exit()
        
        # looping through every number from 1 to n. +1 so th nth number is inclusive.
        for i in range(1, n + 1):
            # print(i)
            # defining the base case so the first three numbers are accounted for.
            if i <= 3:
                result = 1
            else:
                # Subtracting from i, which allows us to look back and use the previous 3 numbers to calculate the next in the sequence.
                result = memoi[i - 1] + memoi[i - 2] + memoi[i - 3]
            # Save the computed fib number
            memoi[i] = result
        
        return memoi[n]


class UserTools:
    # This method prompts the user for input.
    @staticmethod
    def get_input() -> int:
        """
        - This static method prompts the user to enter a number.
        - It also keeps asking until the user enters a positive number.
        """
        while True:
            try:
                user_input: int = int(input(f"\nPlease enter a number\n:"))

                if not isinstance(user_input, int):
                    raise ValueError
                else:
                    return user_input
                
            except ValueError as e:
                print(f"\nYou must enter a number and make sure it is a whole number")


    # This method simulates the scrolling text at the begginning of a star wars movie.
    # Well, at least i think it does :)
    @staticmethod
    def star_wars_crawl(text: str, line_width: int = 70, speed: float = 0.3, tilt: float = 0.8):
        """
        Print `text` as a simple Star Wars style intro crawl in the terminal.

        - line_width: wrapping width for paragraphs
        - speed: delay between frames (seconds)
        - tilt: how much left indentation increases with depth
        """
        cols, rows = shutil.get_terminal_size(fallback=(80, 24))
        lines = []

        # Wrap paragraphs into lines
        for para in text.strip().splitlines():
            if not para.strip():
                lines.append("")  # keep blank line as spacer
                continue
            for w in textwrap.wrap(para.strip(), width=line_width):
                lines.append(w)
            lines.append("")  # small gap between wrapped paragraphs

        # Extra vertical padding so text starts off-screen
        pad_top = rows

        # Animate: slide the text up; more indent for deeper lines lets call it simulating perspective hehe
        for offset in range(pad_top + len(lines) + rows):
            os.system("cls" if os.name == "nt" else "clear")
            start = max(0, offset - pad_top)
            end = min(len(lines), offset)
            visible = lines[start:end]

            for i, line in enumerate(visible):
                depth = len(visible) - i  # lines farther away will have bigger depth
                indent = max(0, int(tilt * depth))
                # center after indent, but don’t let it go negative
                remaining = max(0, cols - indent - len(line))
                center_pad = remaining // 2
                print(" " * (indent + center_pad) + line)

            time.sleep(speed)

def main():
    # UserTools.star_wars_crawl(text)
    #*********** uncomment the line above if you are running this in VScode to see something cool**************
    # Prompting the user for input
    user_input = UserTools.get_input()
    # Instantiating the do the fib class with the positive integer th euser entered
    fibs = DoTheFib(user_input)
    # calling the caluclate fib method and printing the output
    print(f"You entered the number: {user_input}, the {user_input}th number in the tribonacci sequence is {fibs.calculate_fib()}")


if __name__ == "__main__":
    main()