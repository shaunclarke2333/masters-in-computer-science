

# importing depenencies
import math
import random
import os


# This function accepts the user_menu input
def user_menu_input():
    # Tuple to hold the options if user wants prgram to choose
    program_chooses = (1,2)

    try:
        # Asking the user to eneter their menu selection
        user_input = int(input(f"Lets Play A Game ...\n1. Yes\n2. No\n3. You Choose\n\nSo what will it be, 1, 2, or 3? ...\n:> "))
        # Logic to validate user input and proceed accordingly. 
        if user_input >= 1 and user_input <= 3:
            if user_input == 1 or user_input == 2:
                return user_input
            elif user_input == 3:
                # Getting a random option from the program_chooses tuple.
                user_input = random.choice(program_chooses)
                return user_input
    except ValueError:
            return False
    
x = user_menu_input()

if not x:
        print("False")
else:
        print(x)

# This function uses the random module to generate a random number
def generate_random_number():
    number = random.randint(1,100)

# This function gets the user guess via input and makes sure it's an int
def get_user_guess():
    try:
        # Asking the user to enter their guess
        user_input = int(input(f"Enter your guess young Jedi? (1-100)\n:> "))
        return user_input
    except ValueError:
        return False
    
def check_guess(random_number, user_guess):
    #  random_win_response = ["Winner, winner chicken dinner", "You are correct"]
     if random_number == user_guess:
          return True
     elif user_guess > random_number:
        pass
            