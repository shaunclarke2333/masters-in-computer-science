class Queue:
    def __init__(self):
        self.a_in = []
        self.a_out = []
        self.cheap: int = 0 # Keeps track of cheap operations
        self.costly: int = 0 # # Keeps track of costly operations
    def enqueue(self, data):
        self.a_in.append(data)
        # Counting enqueueing as cheap
        self.cheap += 1
        # print(self.a_in)
        # print(self.a_out)
    def dequeue(self):
        if (self.a_out == []):
            while len(self.a_in) > 0:
                self.a_out.append(self.a_in.pop())
        # print(self.a_in)
        # print(self.a_out)
        else:
            # handle error if trying to dequeue an empty operation
            raise IndexError("dequeue from empty queue")
        
        # Doing this
        val = self.a_out.pop()
        # Just so i can count it here
        self.cheap += 1
        # print(self.a_in)
        # print(self.a_out)
        return val


def main():
    # Which operations are cheap or costly?
    q = Queue()
    q.enqueue(1) # 
    print("********")
    q.enqueue(2) # 
    print("********")
    q.enqueue(3) # cheap
    print("********")
    q.dequeue() # 
    print("********")
    q.dequeue() # 
    print("********")
    q.dequeue() # 

main()