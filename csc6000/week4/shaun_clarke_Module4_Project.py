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
num_arrangements_input = int(input(f"Total number of the arrangement you must enter, no greater than {subsets_input_total} it should be:\n:> "))

# list to hold factorial outputs
factorial_of_subsets_list = []
# looping through the input string
for subset in list_of_subet_inputs:
    # calling the factorial function and appending the output to the list
    factorial_of_subsets_list.append(factorial(subset))


print(f"This is factorial list: {factorial_of_subsets_list}")
print(f"This is input integer list: {list_of_subet_inputs}")

# list = [2, 3, 4, 2]

num_of_the_arrangement = num_arrangements_input

# creating a list of lists that hold the ranges of each subset
list_of_ranges = []
for i in range(len(list_of_subet_inputs)):
    ranges = []
    for x in range(0,list_of_subet_inputs[i]+1):
        ranges.append(x)
    list_of_ranges.append(ranges)
# print(f"This is list of ranges: {list_of_ranges}")

# Going through the subset ranges to get possible combinations
final_combinations_list = [[]]
for range in list_of_ranges:
    new_combinations = []
    for combination in final_combinations_list:
        for value in range:
            new_combination = combination + [value]
            new_combinations.append(new_combination)
    final_combinations_list = new_combinations

# Getting only valid combinations that are not greater than number of the arrangement
valid_combinations = []
for combo in final_combinations_list:
    if sum(combo)== num_of_the_arrangement:
        valid_combinations.append(combo)

# Solving for total number of arrangements
all_combo_factorials = 1
for combo in valid_combinations:
    print(f"This is combo: {combo}")
    combo_factorial_divisor = 1
    for value in combo:
        if value == 0:
            value += 1
        combo_factorial_divisor *= value
    print(f"This is combo factorial divisor: {combo_factorial_divisor}")
    #calling the factorial function 
    num_items_in_combo = len(combo)
    print(f"This is combo length: {num_items_in_combo}")
    print(f"This is combo length type: {type(num_items_in_combo)}")
    # combo_facorial_numerator = factorial(num_items_in_combo)
    # print(f"This is factorial numerator: {combo_facorial_numerator}")
    all_combo_factorials += combo_factorial_divisor
print(all_combo_factorials)
