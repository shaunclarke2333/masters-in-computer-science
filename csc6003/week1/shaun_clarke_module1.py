

# importing depenencies
import math
import random


# This function accepts the user_menu input
def user_menu_input():
    # Tuple to hold the options if user wants prgram to choose
    program_chooses = (1,2)

    try:
        # Asking the user to eneter their menu selection
        user_input = int(input(f"Lets Play A Game ...\nI guess a number between 1 and 100 and you tell me what it is ...\n\n1. Yes\n2. No\n3. You Choose\n\nSo what will it be, 1, 2, or 3? ...\n:> "))
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
    
# This function uses the random module to generate a random number
def generate_random_number():
    number = random.randint(1,100)
    return number

# This function gets the user guess via input and makes sure it's an int
def get_user_guess():
    try:
        # Asking the user to enter their guess
        user_input = int(input(f"What number did you guess young Jedi? (1-100)\n:> "))
        return user_input
    except ValueError:
        return False

# This function checks if the user's guess is correct    
def check_guess(random_number, user_guess):
    if random_number == user_guess:
        return "winner"
    elif user_guess > random_number:
        return "high"
    elif user_guess < random_number:
        return "low"

# This function provides hints
def give_hint(random_num):
    # list to hold relevant hints
    hints_list = []

    # checking if random number is a multiple of 5
    if random_num % 5 == 0:
        hints_list.append("The number is a multiple of 5")
    
    # Checking if number is even
    if random_num % 2 == 0:
        hints_list.append("The number is even")

    # Checking if number is odd
    if random_num % 2 != 0:
        hints_list.append("The number is odd")

    # Checking if number to exp 2 > 1000
    if random_num ** 2 > 1000:
        hints_list.append("The number to the power of 2 is grater than 1000")
    
    # Checking if number to exp 2 < 1000
    if random_num ** 2 < 1000:
        hints_list.append("The number to the power of 2 is less than 1000")

    return hints_list


def main():
    # While loop to present the user with a menu and process their input
    while True:
        try:
            # getting the user input and validating it
            menu_input = user_menu_input()

            # validating function output
            if menu_input == 1:
                print(f"\nWe have a brave one among us, let's begin ...")
                break
            elif menu_input == 2:
                print(f"\nSeems like we won't be playing, live long and prosper *_*_* ...", end="\n\n")
                exit()
            elif not menu_input:
                # Raising a value error if input doesn't match criteria
                raise ValueError(f"\nFocus young Jedi, enter 1, 2 or 3 ...\n")
        except ValueError as err:
            print(err)

    # Generating the random number the user will try to guess
    random_num = generate_random_number()

    # generating hints
    hints = give_hint(random_num)
    # Counter to keep track of guesses
    guess_counter = 1

    # While loop that allows user to guess until they get it right.
    while True:
        try:
            # Getting the user guess input and processing it
            user_guess = get_user_guess()

            # Validating user_guess output to make sure the user stays within range
            if user_guess < 1 or user_guess > 100:
                raise ValueError(f"\nTry again, make sure you enter a number with the range 1-100\n")
            
            # Counting each guess
            guess_counter += 1
            
            # Checking the user's guess
            guess = check_guess(random_num, user_guess)
            
            # Logic to process the guess function output and print to the console accordingly
            if guess == "winner":
                print(f"\nWINNER WINNER CHICKEN DINNER!!")
                print(f"You got lucky on your {guess_counter} attempt!")
                break
            elif guess != "winner" and guess_counter > 2:
                # chose a random more detailed hint
                raise ValueError(f"\n{random.choice(hints)}\n")
            elif guess == "high":
                raise ValueError(f"\nTry again but lower\n")
            elif guess == "low":
                raise ValueError(f"\nTry again but higher\n")
        except ValueError as err:
            print(err)
        


if __name__ == "__main__":
    main()
