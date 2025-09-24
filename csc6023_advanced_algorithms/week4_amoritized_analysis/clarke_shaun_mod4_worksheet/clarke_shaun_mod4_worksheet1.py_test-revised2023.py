
"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 4 Amoritized Analysis
Task:
    Worksheet Task 01
    
    Run the Dynamic Array test function trying to find values of initialSize and probRemove that delivers a probability of costly operations of at least 1%.
    "Try" is the key word in the previous sentence.
    If you can't do it, include comments explaining why it is not possible (or easy to do) and the significance of that point.
    
"""


from random import randrange

def test(initialSize, probRemove):
    accCheap, accCosty = 0, 0
    s = initialSize
    m = 2*s
    for i in range(100000):
        if (randrange(100) < probRemove):
            if (s > 0):
                s -= 1
        else:
            if (s == m):
                m = m*2
                s += 1
                accCosty += 1
            else:
                s += 1
                accCheap += 1
    print("Initial size:", initialSize, "Prob Remove:", probRemove, "out of 100")
    print("Costy: {:7} ({:3.1}%)".format(accCosty,100*accCosty/(accCosty+accCheap)))
    print("Cheap: {:7} ({:3.1}%)".format(accCheap,100*accCheap/(accCosty+accCheap)))

def main():
    test(1, 20)
    test(1, 40)
    test(2, 10)
    test(2, 30)
    test(5, 20)
    test(5, 40)
    test(10, 30)
    test(20, 10)

    """
    A costly step only happens when the array is full and has to double its size. Since doubling makes the array grow really fast (2, 4, 8, 16, …),
    it doesn’t happen often.
    So the fact that these expensive steps are rare and spread out. On average, each operation still takes about the same small amount of time.
    Which is why appending to a dynamic array will be constant time on averageish.

    """

    """
    Output
Initial size: 1 Prob Remove: 20 out of 100
Costy:      15 (0.02%)
Cheap:   79942 (1e+02%)
Initial size: 1 Prob Remove: 40 out of 100
Costy:      14 (0.02%)
Cheap:   60212 (1e+02%)
Initial size: 2 Prob Remove: 10 out of 100
Costy:      15 (0.02%)
Cheap:   89872 (1e+02%)
Initial size: 2 Prob Remove: 30 out of 100
Costy:      14 (0.02%)
Cheap:   70259 (1e+02%)
Initial size: 5 Prob Remove: 20 out of 100
Costy:      13 (0.02%)
Cheap:   80069 (1e+02%)
Initial size: 5 Prob Remove: 40 out of 100
Costy:      12 (0.02%)
Cheap:   60228 (1e+02%)
Initial size: 10 Prob Remove: 30 out of 100
Costy:      11 (0.02%)
Cheap:   69851 (1e+02%)
Initial size: 20 Prob Remove: 10 out of 100
Costy:      11 (0.01%)
Cheap:   90014 (1e+02%)
    """

main()
