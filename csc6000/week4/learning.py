# This is how we will calculate factorials:
def factorial (num):
    total = 1 # total starts at 1 because multiplying by 0 will zero everything
    for i in range(1,num+1): # Starting range at one for the same reason
        # print(f"This is i: {i}")
        total *= i
    # print(f"Total: {total}")
    # print("The total is: {}".format(total))
    return total


# getting all options of each


# def multiset_arrangement_function (list_of_subet_inputs):
#     num_of_elements = 0
#     subset_factorials_total = 1

#     for subset in list_of_subet_inputs:
#         num_of_elements += subset
#         subset_factorials_total *= factorial(subset)
#     return factorial(num_of_elements)//subset_factorials_total

# print(multiset_arrangement_function([2,1,1]))

list = [2, 3, 4, 2]

num_of_the_arrangement = len(list)

list_of_ranges = []
for i in range(len(list)):
    ranges = []
    for x in range(0,list[i]+1):
        ranges.append(x)
    list_of_ranges.append(ranges)
# print(f"This is list of ranges: {list_of_ranges}")

final_combinations_list = [[]]
for range in list_of_ranges:
    new_combinations = []
    for combination in final_combinations_list:
        for value in range:
            new_combination = combination + [value]
            new_combinations.append(new_combination)
    final_combinations_list = new_combinations

valid_combinations = []
for combo in final_combinations_list:
    if sum(combo)== num_of_the_arrangement:
        valid_combinations.append(combo)

all_combo_factorials = 1
for combo in valid_combinations:
    print(f"This is combo: {combo}")
    combo_factorial = 1
    for value in combo:
        if value == 0:
            value += 1
        combo_factorial *= value
    print(f"This is combo factorial: {combo_factorial}")
    all_combo_factorials += combo_factorial
print(all_combo_factorials)

