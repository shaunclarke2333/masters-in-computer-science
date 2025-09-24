
"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 4 Amoritized Analysis
Task:
    Worksheet Task 01
    
    Implement a Double Array Queue and test it for a very large case (100,000 randomly decided operations of enqueue or dequeue)

    Your program should keep track of the number of costly operations and cheap operations and print them after running.

    At the beginning of its run, your program should also ask the user about the ratio between enqueue and dequeue operations:

    The probability of enqueues and dequeues should always be within the 33-67% range and should always add up to 100% (33% enqueues - 67% dequeues or 67% enqueues - 33% dequeues or anything in between)
    Your program should then simulate 100,000 operations according to the probability input by the user.
    All of the enqueues and all of the dequeues should not happen consecutively but randomly according to the input probability.
    If your program does all of enqueues and then all of the dequeues, it would not be very interesting to see how many costly and cheap operations there were.

    Some other things to keep in mind:

    Make sure the program does not crash if you try to do a dequeue operation on an empty double array queue. You can do this with simple try/except blocks.
    Do not get double array queues mixed up with the dynamic array data structure or the test function used in the worksheet.
    Although amortized analysis is useful with respect to dynamic arrays as well as double array queues, this assignment is only on double array queues. 
    Do not change the basics of the double array queue implementation, though you may add to it.
    For example, you may want to add attributes to the class such as self.cheap and self.costly to keep track of the cheap and costly operations. 
    Obviously you will need to keep track of cheap and costly operations.
    You may do so using an object oriented programming approach where you have self.cheap and self.
    costly attributes as part of the class which can be incremented in the enqueue and dequeue methods OR you may keep track of these in your main code.
    I recommend using the object oriented approach. 
    
"""
from random import randrange

class UserInput:
    @staticmethod
    def get_enqueue_probability() -> int:
        """
        - Prompts the user to enter the enqueue probability (33–67).
        - Keeps asking until the user enters a valid integer in the range.
        - The dequeue probability is automatically 100 - enqueue probability.
        """
        while True:
            try:
                p_enq: int = int(input("Enter enqueue probability (33–67): ").strip())
                if 33 <= p_enq <= 67:
                    return p_enq
                else:
                    print("\nYou must enter an integer between 33 and 67 (inclusive).")
            except ValueError:
                print("\nYou must enter a whole number.")



class Queue:
    def __init__(self):
        self.a_in = []
        self.a_out = []
        # ADD: counters for amortized-cost tracking
        self.cheap = 0    # counts cheap ops (regular pushes/pops)
        self.costly = 0   # counts costly ops (the bulk transfer a_in -> a_out)
    
    def enqueue(self, data):
        self.a_in.append(data)
        # ADD: enqueue is a single push -> cheap
        self.cheap += 1
        # print(self.a_in)
        # print(self.a_out)


    def dequeue(self):
        # If out stack empty but in stack has items, we must transfer (costly event).
        if (self.a_out == []):
            if len(self.a_in) > 0:
                # ADD: count ONE costly operation for the entire transfer
                self.costly += 1
                while len(self.a_in) > 0:
                    self.a_out.append(self.a_in.pop())
            else:
                # ADD: nothing to dequeue; raise to let caller handle safely
                raise IndexError("dequeue from empty queue")

        # The actual pop from a_out is a cheap operation
        val = self.a_out.pop()
        self.cheap += 1
        # print(self.a_in)
        # print(self.a_out)
        return val

def main():
    # prompting user to enter the enqueue probability (33–67).
    p_enq: int = UserInput.get_enqueue_probability()
    
    # Calculating the dequeue probability.
    p_deq: int = 100 - p_enq
    print(f"Using probabilities: enqueue={p_enq}%, dequeue={p_deq}%")

    # Instantiating the Queue class
    q: int = Queue()

    # Simulating 100,000 random operations according to the probability input by the user.
    data_counter: int = 0
    TOTAL_OPS: int = 100000

    for _ in range(TOTAL_OPS):
        # Randomizing the operations so they won't happen in blocks all at once.
        if randrange(100) < p_enq:
            # enqueue path (cheap)
            data_counter += 1
            q.enqueue(data_counter)
        else:
            # dequeue path: protect against empty queue
            try:
                q.dequeue()
            except IndexError:
                # Safe to ignore (assignment requires: do not crash on empty dequeues)
                pass

    total_counted: int = q.cheap + q.costly
    costly_pct: int = (100.0 * q.costly / total_counted) if total_counted else 0.0
    cheap_pct: int  = (100.0 * q.cheap  / total_counted) if total_counted else 0.0

    print("\n=== Double Array Queue Simulation Results ===")
    print(f"Total operations counted: {total_counted:,}")
    print(f"Costly operations: {q.costly:,} ({costly_pct:.3f}%)")
    print(f"Cheap operations:  {q.cheap:,}  ({cheap_pct:.3f}%)")


if __name__ == "__main__":
    main()