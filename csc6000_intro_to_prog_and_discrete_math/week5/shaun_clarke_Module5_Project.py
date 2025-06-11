"""
Instructions
Write a Python program to print Pascal's Triangle.

Your program should ask the user the number of lines (use a limit from 4 to 8 lines) of the Pascal's Triangle;
Your program should have a function that computes the binomial coefficient of n and k, and this function should be used to find the values of the cells of the Pascal's Triangle;
The great challenge of this program is the output formatting which requires you to assemble the lines with the proper space.
"""

#Psuedo coding it
"""
Ask for input
So whatever limit the user enters, we will loop through that limit plus 1 so we get the number of rows for the triangle.
We do plus 1 because index starts at 0 in the loop and stops just before the actual number we are looping through.
So looping through 4 + 1 will give us 0,1,2,3,4. The rows of the triangle from 0 to 4.
Looking at pascals triangle while using the formula (n,k) with n at the top of the parenthesis and k at the bottom.
You see that k in each cell of the triangle is the range of the row number plus 1. so if it is row 3, k in each of the three cells would be 0,1,2,3.
Keep in mind the triangle starts from row 0.
generator expression might help with getting max width of the printed rows

"""

# this function gets the user input
def get_user_input():
    """
    This function gets and validates the user input.
    It makes sure the input meets the set criteria
    """
    # variale to hold the final user input that will be the numbe rof lines
    triangle_lines = ""
    # While loop to make sure the user enters the correct input before it moves on
    while triangle_lines != int:
        try:
            get_input = input(f"Your mission if you choose to accept it ...\nEnter a number from 4 to 8, to create Pascal's Triangle.\nEnter Number:> ")
            print("")

            # Allowing the user to exit the program
            if get_input == "exit":
                exit()
            
            # Converting the input to an integer
            get_input =int(get_input) 
            
            # Making sure it meets the set criteria
            if get_input >= 4 and get_input <= 8:
                triangle_lines = get_input
                print(f"You've entered {triangle_lines}, Now watch the magic happen ...")
                print(f" ")
                break
                
            else:
                # Raising a value error if the number entered does not fit the range
                raise ValueError
        except ValueError:
            print(f"You missunderstood the mission objective, please try again ...")
            print("")

    return triangle_lines

# This function calculates the binomial coefficient of a number
def comb_calc(n,k):
    # n!/k!(n-k)!
    """
    This function calculates the Binomial Coefficient of a number.
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

# Pritns pascals triangle
def print_pascals_triangle():
    """
    This function prints pascals triangle using the following helper functions:
    get_user_input()
    comb_calc()
    """
    triangle_lines = get_user_input()
    # List to hold all rows of the triangle
    all_rows = []
    # For loop to get the range for each line, basically getting k for each cell of each line.
    for n in range(triangle_lines +1):
        # Empty list to hold the individual range for each line.
        each_range = []
        for i in range(n + 1):
            each_range.append(i)
    
        # List to hold trinagle row
        each_row = []
        # calculating triangle cells
        for k in each_range:
            each_row.append(comb_calc(n,k))
        
        # making the each_row a spaced string instead of separate items then appending it
        all_rows.append(' '.join((map(str,each_row))))

    # Using a generator expression to get the max width by getting the max length of each string in the list of lists.
    max_width = max(len(row) for row in all_rows)

    # printing eaxh row in the list
    for row in all_rows:
        # printing everything with the same max width so they will all be automatically centered.
        print(f"{row:^{max_width}}")

def main():
    print_pascals_triangle()

if __name__ == "__main__":
    main()
