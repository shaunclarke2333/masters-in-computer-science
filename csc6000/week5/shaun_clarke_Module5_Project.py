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


"""

def get_user_input():
    triangle_lines = ""
    while triangle_lines != int:
        try:
            get_input = input(f"Your mission if you choose to accept it ...\nEnter a number from 4 to 8, to create Pascal's Triangle.\nEnter Number:> ")
            print("")

            if get_input == "exit":
                exit()

            get_input =int(get_input) 
            
            if get_input >= 4 and get_input <= 8:
                triangle_lines = get_input
                print(f"You've entered {triangle_lines}, Now watch the magic happen ...")
                break
            else:
                raise ValueError
        except ValueError:
            print(f"You missunderstood the mission objective, please try again ...")
            print("")

# get_user_input()