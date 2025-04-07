"""
**Instructions**
Write a Python program that:

○ Asks the user a scale factor a and a common ratio r;

○ Your program inform the user if the GP informed converges to a sum regardless of its number of elements:

■ If the GP converges to a sum regardless of the number of elements, your program should compute the sum of infinite elements;

■ Otherwise, your program should ask the number of elements n, and compute the sum of all elements;

○ With that information, your program should print out the first 3 elements of the GP and the computed sum.

For example, if the user enters: a = 10 and r = 0.5, your program should output:

This GP converges with infinite elements to 20
the first terms are 10, 5, and 2.5

For example, if the user enters: a = 10 and r = -0.5, your program should output:

This GP converges with infinite elements to 6.6666667
the first elements are 10, -5, and 2.5

For example, if the user enters: a = 1 and r = 2, your program should output:

This GP does not converge to a finite number with infinite elements and ask for n, and if the user enters n = 10, the final output should be:

This GP sum with 10 elements is equal to 1023
the first elements are 1, 2, and 4
"""

# This function makes sure output is and integer or float
def check_number(number):
    """
    This function makes sure output is and integer or float
    It use is_integer() to check if a float can be represented as an integer
    without losing precision.
    """
    
    final_number = ""
    if number.is_integer():
        final_number = int(number)
    else:
        final_number = number
    return final_number

# Function to get the first three elements
def get_frist_three_terms(a,r):
    """
    iterating through the formula to find the first three terms and adding each term to the list
    """
    three_terms_list = []
     # iterating through the formula to find the first three terms and adding each term to the list
    for i in range(1,4):
        # print(i)
        ans = check_number(a*r **( i-1))
        three_terms_list.append(ans)

    return three_terms_list
    
# Function to ask for user input
def get_input():

    """
    Ask the user to enter a scale factor or common ratio
    """

    # Variables
    a=""
    r= ""

    # While loop to ensure that the user enters scalar number as input.
    while type(a) != int or type(a) != float:

        try:
            get_input = input(f"Enter a scale factor(a) you must, a number it should be: ")
            print("")

            if get_input == "exit":
                exit()

            a = float(get_input) 
            if a.is_integer():
                a = int(a)

            if type(a) == int or type(a) == float:
                break

        except ValueError:
            print(f"Lets try this again Young Jedi...")
            print("")

    # While loop to ensure that the user enters common ratio number as input.
    while type(r) != int or type(r) != float:

        try:
            get_input = input(f"Enter a common ratio(r) you must, a number it should be: ")
            print("")

            if get_input == "exit":
                exit()

            r = float(get_input)
            if r.is_integer():
                r = int(r)

            if type(r) == int or type(r) == float:
                break
            
        except ValueError:
            print(f"Lets try this again Young Jedi...")
            print("")

    return a,r

# Function to get the specific sum of a geometric progression
def sum_gp(a, r):
    """
    **Instructions**
    Write a Python program that:

    ○ Asks the user a scale factor a and a common ratio r;

    ○ Your program inform the user if the GP informed converges to a sum regardless of its number of elements:

    ■ If the GP converges to a sum regardless of the number of elements, your program should compute the sum of infinite elements;

    ■ Otherwise, your program should ask the number of elements n, and compute the sum of all elements;

    ○ With that information, your program should print out the first 3 elements of the GP and the computed sum.
    """
    if r == -1:
        # print(f"Minus 1")
        print("This GP does not converge to a finite number with infinite elements")
        user_input = input(f"Please enter the number of elements in the Geometric Progression: ")

        # converting input to integer
        nth_term = int(user_input)

        negative_one_total = 0
        for i in range(nth_term):

            ans = a * (r)**i
            ans = check_number(ans)

            negative_one_total += ans
            print(ans)

        # Calling function to to find the first three terms
        frist_three_terms = get_frist_three_terms(a,r)

        print(f"This GP sum with {nth_term} elements is equal to {negative_one_total}")
        print(f"The first terms are {frist_three_terms[0]}, {frist_three_terms[1]}, and {frist_three_terms[2]}")

    elif r == 1:
        # print(f"Equals 1")
        print("This GP does not converge to a finite number with infinite elements")
        user_input = input(f"Please enter the number of elements in the Geometric Progression: ")

        # converting input to integer
        nth_term = int(user_input)

        sum = a * nth_term
        sum = check_number(sum)

        # Calling function to to find the first three terms
        frist_three_terms = get_frist_three_terms(a,r)

        print(f"This GP sum with {nth_term} elements is equal to {sum}")
        print(f"The first terms are {frist_three_terms[0]}, {frist_three_terms[1]}, and {frist_three_terms[2]}")

    elif r < 1:
        # Calculating the infinite sum
        infinite_sum = (a /(1-r))

        infinite_sum = check_number(infinite_sum)
        # Calling function to to find the first three terms
        frist_three_terms = get_frist_three_terms(a,r)

        print(f"This GP converges with infinite elements to {infinite_sum}")
        print(f"The first terms are {frist_three_terms[0]}, {frist_three_terms[1]}, and {frist_three_terms[2]}")
    
    elif r > 1:
        # print(f"Greater")
        print("This GP does not converge to a finite number with infinite elements")
        user_input = input(f"Please enter the number of elements in the Geometric Progression: ")

        # converting input to integer
        nth_term = int(user_input)

        finite_sum = a * (1 - r ** nth_term)/(1-r)
        finite_sum = check_number(finite_sum)

        # Calling function to to find the first three terms
        frist_three_terms = get_frist_three_terms(a,r)

        print(f"This GP sum with {nth_term} elements is equal to {round(finite_sum)}")
        print(f"The first terms are {frist_three_terms[0]}, {frist_three_terms[1]}, and {frist_three_terms[2]}")

# Getting user input
a,r = get_input()

sum_gp(a,r)
