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

# Parent class with factorial method
class arrangements:
    def __init__(self):
        pass

# This is how we will calculate factorials:
def factorial (num):
    total = 1 # total starts at 1 because multiplying by 0 will zero everything
    for i in range(1,num+1): # Starting range at one for the same reason
        # print(f"This is i: {i}")
        total *= i
    # print(f"Total: {total}")
    # print("The total is: {}".format(total))
    return total


num_of_subsets = int(input(f"Enter a number of subsets you must ...\nNo less than 3 and no greater than 8 they should be:\n:> "))

subsets_input = input(f"{num_of_subsets} subsets you have, the size of each you must enter, comma separated.\nNo less than 1 and no greater than 5 each size should be\n:> ")

# Splitting the input string to create a list
subsets_input = subsets_input.split(",")

# print(type(subsets_input))
list_of_subet_inputs = list(map(int,subsets_input))

# sum of all the subset elements to get the total elements
subsets_input_total = sum(list_of_subet_inputs)

print(f"type: {list_of_subet_inputs}")

# Asking the user for the total number of arrangements:
num_arrangements_input = int(input(f"Total number of arrangements you must enter, no greater than {subsets_input_total} it should be:\n:> "))

# # list to hold factorial outputs
# factorial_of_subsets_list = []
# # looping through the input string
# for subset in list_of_subet_inputs:
#     # calling the factorial function and appending the output to the list
#     factorial_of_subsets_list.append(factorial(subset))


# print(f"This is factorial list: {factorial_of_subsets_list}")
# print(f"This is input integer list: {list_of_subet_inputs}")


# def multiset_arrangement_function (factorial_of_subsets_list, list_of_subet_inputs):
#     # The total number of elements
#     subsets_total = sum(list_of_subet_inputs)
#     print(f"sum of subsets: {subsets_total}")

#     # getting factorial for total elements in subset
#     subset_total_factorial = factorial(subsets_total)
#     print(f"This is subset total factorial: {subset_total_factorial}")

#     # Variable to hold total for all factorials after being multiplied
#     factorials_total = 1

#     for subset_factorial in factorial_of_subsets_list:
#         factorials_total *= subset_factorial

#     print(f"This is ans: {subset_total_factorial//factorials_total}")

# multiset_arrangement_function(factorial_of_subsets_list, list_of_subet_inputs)
