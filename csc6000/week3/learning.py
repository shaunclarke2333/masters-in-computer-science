# print(f"Arithmetic Progression is when you add the common difference to the previous number in the sequence.\nCommon difference is how much the sequence increments by.")
# for i in range(20, 1, -3):
#     print(f"Incrementing by a commond difference of 3: {i}")


# def ap(a, n, d):
#     ans = a + (n-1)*d
#     print(f"Your initial term is {a}, the common difference is {d}, the N'th term is {n}")
#     print(f"The 1oooth element is: {ans}")

# print(f"Calling ap")
# ap(5605,8,17)

# print(f"This is finding the 8th term in the sequence")
# print(list(range(5605,5724,17)))

# # Using the Gauss method to calculate the sum of 1 to the nth number
# def gauss(n):
#     print(f"Using the Gauss method to calculate the sum of 1 to {n}")
#     print(n * (n+1)//2)

# gauss(1013)

# def summation(i):
#     total = 0
#     empty_list = []
#     for x in range(i):
#         x += 1
#         item = (2*x+1)
#         total += item
#         empty_list.append(item)
        
#     print(f"The total using summation is: {total}")
#     print(empty_list)
    
# summation(4)

# def summationap(first_term, com_diff, num_of_terms):
#     """
#     Using Summation Notation formula.
    
#     """
#     sum_ap = 0
#     for i in range(num_of_terms):
#         add_up = (first_term + i * com_diff)
#         sum_ap += add_up
#         print(add_up)
#     print("")
#     print(f"This is the total using summation on an arithemetic progression: {sum_ap}")
       
# summationap(2,4,7)

def geometric_progression_nth_term(first_term, common_ratio, num_term):
    """
    Using the formula to find the Nth term in geometric progression
    R is the common ratio, similar to common difference
    N is the specific term you want to find in this case.
    First term or a sub 1 is the first term in teh sequence.
    formula = first_term * r ** Nth_term - 1
    """
    # # Calculate exponent first
    # exoponent = num_term - 1
    
    # # calculating common ratio raised to exponent 
    # ratio_raised_to_exponent = common_ratio ** exoponent

    # # multiply first item in GP sequence by the ruslt of the ratio raised to the exponent
    # ans = ratio_raised_to_exponent * first_term
    for i in range(num_term):
        # i += 1
        ans = first_term * (common_ratio)** i
        print(ans)


geometric_progression_nth_term(2,-1,5)



# def sum_geometric_progression(r, num_terms, first_term):
#     """
#     This is the formula first_term * (1 - r ** num_terms / 1 - r) but this wont work in python.
#     but using order of operations do the 
#     calculate numerator first.
#     calculate The denominator second
#     Then divide the numerator by the denominator
#     then multiply the remainder by the first_term

#     """
#     numerator = 1 - r ** num_terms
#     denomenator = 1 - r
#     remainder = numerator // denomenator

#     ans = first_term * remainder
    
#     print(f"Thi is top: {numerator}, This is bottom: {denomenator}, this is remainder: {remainder}")
#     print(f"This is answer: ans {ans}")


# sum_geometric_progression(3,5,2)

# def infinite_gp_sum(a,r):
#     print(round((a/(1-r)),1))

# infinite_gp_sum(10, -0.5)



