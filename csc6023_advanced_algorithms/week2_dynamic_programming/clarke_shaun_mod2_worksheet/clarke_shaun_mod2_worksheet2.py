"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 2 Dynamic Programming
Task:
    Worksheet Task 02
    Implement a recursive program that asks the number of disks and delivers the minimal number of moves to solve the Towers of Hanoi efficiently
    Your program must have a recursive function that delivers the number of movements for a given number of disks; it does NOT need to give the moves themselves.
    T(n)=2T(n−1)+1
"""
import time
import os

# to clear the screen on any system.
def clear():
    # This should work for whatever system its is being graded on Windows and Mac/Linux.
    os.system('cls' if os.name == 'nt' else 'clear')

# Setting the fuse 
def fireworks(n=5):
    # n = for the number of frames
    for step in range(1, n+1):
        clear()
        print(" " * (10-step) + "*")          # left side bang
        print(" " * 10 + "*")                 # center bang
        print(" " * (10+step) + "*")          # right side bang
        print("\n" * step)                    # move down each frame and more bang
        time.sleep(0.5)



def moves(num_disks: int) -> int:
    """
    This static method takes number of disks as input and calculates the number of moves required.
    """
    # If no disks then no moves.
    if num_disks == 0:
        return 0
    #Matching the recurrence relation(T(n)=2T(n−1)+1) by reflecting it below in python.
    else:
        #|T(n)=2       T(n−1          ) +1              |
        return 2 * moves(num_disks - 1) + 1




def get_input() -> int:
    """
    This function asks the user for a number input and outputs a number
    """
    while True:
        try:
            # Asking user for input and converting it to an int
            print(f"Your mission if you choose to accept it ...")
            print(f"To save the world you must diffuse the tower of hanoi Bomb...")
            num_input = int(input(f"\nEnter the number of disks to get the shutdown code ...\n:"))
            # If the user inputs an int, break the loop
            break
        # If an int was not entered, raise a value error and promt the user again
        except ValueError as e:
            print(f"\nYour input must be a number ...")
            print(f"\nYou have failed this city ...")
            # pausing so user can see output before the boom
            time.sleep(5)
            # Lighting the match
            fireworks(8)

    return num_input

def main():
    """
    This function is where tie the program together
    """

    # Gettting user input
    user_input = get_input()

    # Calculating how many moves for the number of disks user entered
    number_of_moves = moves(user_input)

    print(f"You entered {user_input} disks, the shutdown code is {number_of_moves}")

if __name__ == "__main__":
    main()

