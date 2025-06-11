"""
Shaun Clarke
CSC6000
Week 7 Assignment

Write a Python program that receives information about a lottery game based on the player guessing k numbers out of n possible numbers. 
Assume that the game consists of the players betting on k numbers, the lottery agent randomly draws k numbers,
and the player wins big if hitting all k drawn numbers, and wins little if hitting k-1 drawn numbers.

Your program should ask the users the values of n and k;
    Then your program should compute:
        the probability of winning big (hitting all k drawn numbers), and
        the probability of winning little (hitting k-1 drawn numbers).
"""

# This function gets the user input
def get_user_input():
    proceed = ""
    # While loop that runs until it is broken, exited or proceed = yes
    while proceed != "yes":
        try:
            # Getting the user input and converting it to lowercase
            user_input = input(f"Shall we play a game? ...\nPlease enter yes or no ...\n:> ").lower()

            # Allowing the user to exit the program
            if user_input == "exit":
                exit()
            
            # Breaking the loop if conditions are met, if not raise a valueerror
            if user_input == "yes":
                print(" ")
                print(f"You have chosen to play a game ...\nYour instructions will follow ...", end="\n\n")
                proceed = user_input
                
                break
            else:
                raise ValueError
        
        except ValueError:
            print(f"Let's try this again ...", end="\n\n")

    n = ""
    while type(n) != int:
        try:
            print(f"This is a lottery simulation game based on you guessing k numbers out of n possible numbers ...", end="\n\n")
            user_input = input(f"Please enter the 'n' number ...\n:>")
            if user_input == "exit":
                exit()

            user_input = int(user_input)
            if type(user_input) == int:
                n = user_input
                print(f"You enterd {n}", end="\n\n")
                break
            else:
                raise ValueError
        except ValueError:
            print(" ")
            print(f"Let's try this again ...", end="\n\n")

    k = ""
    while type(k) != int:
        try:
            user_input = input(f"Please enter the 'K' number, it should be less than {n} ...\n:>")
            if user_input == "exit":
                exit()

            user_input = int(user_input)
            if type(user_input) == int:
                if user_input >= 1 and user_input < n:
                    k = user_input
                    print(f"You enterd {k}", end="\n\n")
                    break
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print(" ")
            print(f"Let's try this again ...", end="\n\n")

    return k,n

# This function simulates the combination formula
def comb_calc(n,k):
    # n!/k!(n-k)!
    """
    This function simulates the combination formula
    """
    # This function calculates the factorial of a number
    def factorial_calc(num):
        factorial = 1
        for i in range(1,num+1):
            factorial*=i
        # print(f"{factorial}")
        return factorial
    
    # Using the formula n!/k!(n-k)! to calculate the answer
    ans = factorial_calc(n)/(factorial_calc(k) * factorial_calc(n-k))

    # Making the number an int if it is or float if it is
    if ans.is_integer():
        return int(ans)
    else:
        return ans

# This function calculates the probability of k numbers out of n
def calc_probability():
    k,n = get_user_input()
    # Variable for 1 because there is only one combination of numbers that can win.
    only_winning_combo = 1

    # Calculating the total number of combinations of winning numbers
    total_possible_combos = comb_calc(n,k)

    # Variable for guessing one less
    k_one_less = k-1

    # calculating combinations of k-1 we can get out of k
    total_combo_k_minus_one_in_K = comb_calc(k,k_one_less)

    # Calculating getting one wrong from the remainin numbers not including winning numbers
    total_combo_of_one_wrong = comb_calc(n-k,1)
    
    print(f"The probability of you hitting all {k} drawn numbers ...\nIs {only_winning_combo}/{total_possible_combos:,}", end="\n\n")
    print(f"the probability of you hitting {k_one_less} of the drawn numbers ...\nIs {total_combo_k_minus_one_in_K}*{total_combo_of_one_wrong}/{total_possible_combos:,}")

def main():
    calc_probability()

if __name__ == "__main__":
    main()