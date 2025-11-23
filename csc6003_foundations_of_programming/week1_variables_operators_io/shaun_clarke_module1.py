# importing depenencies
import random


# This function accepts the user_menu input
def user_menu_input():
    """
    This function takes no parameters.<br>
    It displays the user menu.<br>
    It also prompts the user to make a selection.<br>
    It processes the user input.<br>
    returns the user input as an integer.<br>
    If an invalid input is entered False is returned.
    """
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
    """
    This function takes no parameters.<br>
    Generates a random number between 1 and 100.<br>
    returns the random number as an integer
    """
    number = random.randint(1,100)
    return number

# This function gets the user guess via input and makes sure it's an int
def get_user_guess():
    """
    This function takes no parameters.<br>
    It prompts the user to input their guess.<br>
    The guess must be an integer between 1 and 100.<br>
    The user guess is returned as an integer.<br>
    If an invalid input is entered False will be returned.
    """
    try:
        # Asking the user to enter their guess
        user_input = int(input(f"What number did you guess young Jedi? (1-100)\n:> "))
        return user_input
    except ValueError:
        return False

# This function checks if the user's guess is correct    
def check_guess(random_number, user_guess):
    """
    This function takes two parameters.<br>
    random_number and user_guess.<br>
    It compares the two parameters to see if the user guessed correctly.<br>
    Correct guess returns "winner".<br>
    Guess higher than random_num returns "high".<br>
    Guess lower than random_num returns "low"
    """
    if random_number == user_guess:
        return "winner"
    elif user_guess > random_number:
        return "high"
    elif user_guess < random_number:
        return "low"

# This function provides clue
def give_clue(random_num):
    """
    This function takes one parameter random_num.<br>
    This fucntion calculates the following:.<br>
        even number.<br>
        odd number.<br>
        multiple of 5.<br>
        number to the power of 2 is > 1000.<br>
        number to the power of 2 is < 1000.<br>
    Then returns a list of calculations that apply to the random_num
    """
    # list to hold relevant clue
    clue_list = []

    # checking if random number is a multiple of 5
    if random_num % 5 == 0:
        clue_list.append("The number is a multiple of 5")
    
    # Checking if number is even
    if random_num % 2 == 0:
        clue_list.append("The number is even")

    # Checking if number is odd
    if random_num % 2 != 0:
        clue_list.append("The number is odd")

    # Checking if number to exp 2 > 1000
    if random_num ** 2 > 1000:
        clue_list.append("The number to the power of 2 is grater than 1000")
    
    # Checking if number to exp 2 < 1000
    if random_num ** 2 < 1000:
        clue_list.append("The number to the power of 2 is less than 1000")

    return clue_list

# This function calls the program
def main():
    """
    This function is where the magic happens.<br>
    This is where the the overall logic is organized and ran.<br>
    Also prevents the program from executed if the script is imported.<br>
    """
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
                # Using continue to start over the loop if the user's input doesnt meet criteria.
                print(f"\nFocus young Jedi, enter 1, 2 or 3 ...\n")
                continue
        except ValueError as err:
            print(err)

    # Generating the random number the user will try to guess
    random_num = generate_random_number()

    # generating clue
    clue = give_clue(random_num)
    # Counter to keep track of guesses
    guess_counter = 1

    # While loop that allows user to guess until they get it right.
    while True:
        try:
            # Getting the user guess input and processing it
            user_guess = get_user_guess()

            # Counting each guess
            guess_counter += 1

            # Validating user_guess output to make sure the user stays within range
            if user_guess < 1 or user_guess > 100:
                print(f"\nTry again, make sure you enter a 'number' within the range 1-100\n")
                continue
            
            # Checking the user's guess
            guess = check_guess(random_num, user_guess)
            
            # Logic to process the guess function output and print to the console accordingly
            if guess == "winner":
                print(f"\nWINNER WINNER CHICKEN DINNER!!")
                print(f"You got lucky on your {guess_counter} attempt!")
                break
            elif guess == "high" and guess_counter > 2:
                print(f"\nTry again but lower.\nHeres's a clue:{random.choice(clue)}\n")
            elif guess == "low" and guess_counter > 2:
                print(f"\nTry again but higher.\nHeres's a clue:{random.choice(clue)}\n")
            elif guess == "high":
                print(f"\nTry again but lower.\n")
            elif guess == "low":
                print(f"\nTry again but higher.\n")
        except ValueError as e:
            print(e)
        

if __name__ == "__main__":
    main()
