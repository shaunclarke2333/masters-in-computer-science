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

def get_frist_three_terms(a,r):
    """
    # iterating through the formula to find the first three terms and adding each term to the list
    """
    three_terms_list = []
     # iterating through the formula to find the first three terms and adding each term to the list
    for i in range(1,4):
        # print(i)
        three_terms_list.append(a*r **( i-1))

    return three_terms_list


def sum_gp(a, r):

    if r == -1:
        print(f"Minus 1")
        print("This GP does not converge to a finite number with infinite elements")
        user_input = input(f"Please enter the number of elements in the Geometric Progression: ")

        # converting input to integer
        nth_term = int(user_input)

        negative_one_total = 0
        for i in range(nth_term):

            ans = a * (r)**i

            negative_one_total += ans
            print(ans)

        # Calling function to to find the first three terms
        frist_three_terms = get_frist_three_terms(a,r)

        print(f"This GP sum with {nth_term} elements is equal to {negative_one_total}")
        print(f"The first terms are {frist_three_terms[0]}, {frist_three_terms[1]}, and {frist_three_terms[2]}")

        
  

    elif r == 1:
        print(f"Equals 1")
        print("This GP does not converge to a finite number with infinite elements")
        user_input = input(f"Please enter the number of elements in the Geometric Progression: ")

        # converting input to integer
        nth_term = int(user_input)

        sum = a * nth_term

        # Calling function to to find the first three terms
        frist_three_terms = get_frist_three_terms(a,r)

        print(f"This GP sum with {nth_term} elements is equal to {sum}")
        print(f"The first terms are {frist_three_terms[0]}, {frist_three_terms[1]}, and {frist_three_terms[2]}")
        

    elif r < 1:
        # Calculating the infinite sum
        infinite_sum = (a /(1-r))

        # Calling function to to find the first three terms
        frist_three_terms = get_frist_three_terms(a,r)

        print(f"This GP converges with infinite elements to {infinite_sum}")
        print(f"The first terms are {frist_three_terms[0]}, {frist_three_terms[1]}, and {frist_three_terms[2]}")
    
    elif r > 1:
        print(f"Greater")
        print("This GP does not converge to a finite number with infinite elements")
        user_input = input(f"Please enter the number of elements in the Geometric Progression: ")

        # converting input to integer
        nth_term = int(user_input)

        finite_sum = a * (1 - r ** nth_term)/(1-r)

        # Calling function to to find the first three terms
        frist_three_terms = get_frist_three_terms(a,r)

        print(f"This GP sum with {nth_term} elements is equal to {finite_sum}")
        print(f"The first terms are {frist_three_terms[0]}, {frist_three_terms[1]}, and {frist_three_terms[2]}")

sum_gp(-2, -1)

# Need to do:
"""
Allow user to enter scalar (a) and ratio (r) as input
Add while loops to make sure the user enters the correct item as int and not string.

"""