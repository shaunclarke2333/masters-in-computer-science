"""
Instructions
Solving Arrangements of Multisets

Write a Python program to compute Arrangements of Multisets that:

Asks the user a number of subsets (no smaller than 3, no greater than 8);
j
Asks the user the size of each subset (from 1 to 5);
mi        with i going from 1 to j
Asks the user the total number of the arrangement (a number smaller than the sum of sizes of the subsets - n)
k
Then, it computes and prints the number of arrangements of k elements out of n, considering the subsets of size mi;
"""

# This is how we will calculate factorials:
def factorial_calc(num):
    total = 1 # total starts at 1 because multiplying by 0 will zero everything
    for i in range(1,num+1): # Starting range at one for the same reason
        # print(f"This is i: {i}")
        total *= i
    # print(f"Total: {total}")
    # print("The total is: {}".format(total))
    return total

# This functions validates list input
def validate_input_list(list_item):
    ok = ""
    for item in list_item:
        if item != int:
            ok = "yes"
        else:
            ok = "no"
    return ok

# This function gets all the user input
def get_user_input():
    # Declaring emppty variables to hold input
    j_num_of_subsets = ""
    mi_subsets_input = ""
    k = ""

    while j_num_of_subsets != int:
        try: 
            # Asking user to enter the number of subsets that should be between 3 and 8
            get_input = input(f"Enter a number of subsets you must ...\nNo less than 3 and no greater than 8 they should be:\n:> ")
            print("")
            
            # allowing user to exit program
            if get_input == "exit":
                exit()

            # Converting string input to int
            get_input = int(get_input)

            if  get_input >= 3 and get_input <= 8:
                    j_num_of_subsets = get_input
                    break
            else:
                raise ValueError
        except ValueError:
            print(f"Lets try this again Young Jedi...")
            print("")
                
    while type(mi_subsets_input) != list:

        try:
            # asaking user for their input
            get_input = input(f"{j_num_of_subsets} subsets you have, the size of each you must enter, comma separated.\nNo less than 1 and no greater than 5 each size should be\n:> ")
            print("")

            # allowing user to exit program
            if get_input == "exit":
                exit()

            # Splitting the input string to create a list
            get_input = get_input.split(",")

            # making sure we have a list and that it is not empty and the items are ints
            if type(get_input) == list and len(get_input) == j_num_of_subsets:
                
                # checking if items in list are int
                list_is_int = validate_input_list(get_input)
                if list_is_int == "yes":
                    # converting strings in list to integers.
                    mi_subsets_input = list(map(int,get_input))
                    # print(f"list of subsets: {mi_subsets_input}")
                    break
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print(f"Lets try this again Young Jedi...")
            print("")

    while k != int:
        try: 
            # Asking the user for the total number of arrangements:
            # print(f"This sum of subsets: ")
            get_input = int(input(f"Total number of the arrangement you must enter, no greater than {sum(mi_subsets_input)} it should be:\n:> "))
            # print(f"k number of arrangements input: {k}")
            
            # allowing user to exit program
            if get_input == "exit":
                exit()

            # Converting string input to int
            get_input = int(get_input)

            # making sure that input is less than the sum of the subset sizes
            if  get_input < sum(mi_subsets_input):
                    k = get_input
                    break
            else:
                raise ValueError
        except ValueError:
            print(f"Lets try this again Young Jedi...")
            print("")

    return mi_subsets_input,k


# This function calculates the number of arrangements
def calculate_arrangement_multi(mi_subsets_input,k):
    # sum of all the subset elements to get the total elements
    n_subsets_input_total = sum(mi_subsets_input)
    # print(f"subset input total: {n_subsets_input_total}")

    # calculating numerator by calculating the factorial for the total elements
    numerator = factorial_calc(n_subsets_input_total)
    # print(f"Numerator is: {numerator}")

    # subtracting k from n number of elements
    n_minus_k = n_subsets_input_total - k
    # print(f"This is n minus k: {n_minus_k}")

    # creating new list of all denominators by copying the mi_seubsets list and adding n-k to it
    denominators = mi_subsets_input.copy()
    denominators.append(n_minus_k)

    # creating the total for the factorial total of all numerators
    total = 1
    for item in denominators:
        total *= factorial_calc(item)

    # calculating the answer in formatted output
    print("The number of arrangements of {0} elements out of {1}, considering the subsets of size {2} is: {3}".format(k, n_subsets_input_total, ",".join(map(str, mi_subsets_input)),numerator/total))
    
def main():
    # Calling get user input to get user inputs and assign outputs to variables
    mi_subsets_input,k = get_user_input()
    # print(f"This is j: {j_num_of_subsets}")
    # print(f"This is subsets{mi_subsets_input}")
    # print(f"This is K{k}")

    calculate_arrangement_multi(mi_subsets_input,k)

if __name__ == "__main__":
    main()
