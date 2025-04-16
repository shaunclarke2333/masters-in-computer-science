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
def factorial_calc (num):
    total = 1 # total starts at 1 because multiplying by 0 will zero everything
    for i in range(1,num+1): # Starting range at one for the same reason
        # print(f"This is i: {i}")
        total *= i
    # print(f"Total: {total}")
    # print("The total is: {}".format(total))
    return total

# Asking user to enter the number of subsets that should be between 3 and 8
j_num_of_subsets = int(input(f"Enter a number of subsets you must ...\nNo less than 3 and no greater than 8 they should be:\n:> "))

# asaking user for their input
mi_subsets_input = input(f"{j_num_of_subsets} subsets you have, the size of each you must enter, comma separated.\nNo less than 1 and no greater than 5 each size should be\n:> ")

# Splitting the input string to create a list
mi_subsets_input = mi_subsets_input.split(",")

# converting strings in list to integers.
mi_subsets_input = list(map(int,mi_subsets_input))

print(f"type: {mi_subsets_input}")

# sum of all the subset elements to get the total elements
n_subsets_input_total = sum(mi_subsets_input)

print(f"subset input total: {n_subsets_input_total}")

# Asking the user for the total number of arrangements:
k = int(input(f"Total number of the arrangement you must enter, no greater than {n_subsets_input_total} it should be:\n:> "))
print(f"k number of arrangements input: {k}")

# calculating numerator by calculating the factorial for the total elements
numerator = factorial_calc(n_subsets_input_total)
print(f"Numerator is: {numerator}")

# subtracting k from n number of elements
n_minus_k = n_subsets_input_total - k
print(f"This is n minus k: {n_minus_k}")


mi_subsets_input.append(n_minus_k)

total = 1
for item in mi_subsets_input:
    total *= factorial_calc(item)


print(numerator/total)

# TO DO
"""
TO DO
Now that it works, cleanup code by grouping sections into functions.
Adding error handling.
Adding input verification to ensure user enters integers and not strings.
Ensure user enters items comma separated and each one is an integer.
"""

