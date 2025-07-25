from typing import List

def BFS(V, E):
    for i in range(len(V)):
        V[i] = -1           # all vertices not visited
    count = 0
    for i in range(len(V)):   # for all possible sources
        if (V[i] == -1):
            Q = [i]           # enqueue the source
            print(f"Vertex {verticals[i]} enqueued. Q: {Q}")
            V[i], count = count, count + 1   # visit it
            print(f"Vertex {verticals[i]} visited. V: {V}")
            while (len(Q) != 0):             # for all enqueued
                for e in E:                  # search neighbors
                    if (e[0] == Q[0]) and (V[e[1]] == -1):
                        Q.append(e[1])       # enqueue it
                        print(f"Vertex {verticals[i]} enqueued. Q: {Q}")
                        V[e[1]], count = count, count + 1   # visit it
                        print(f"Vertex {verticals[i]} visited. V: {V}")
                Q.pop(0)                     # dequeue it
                print(f"Vertex {verticals[i]} dequeued. Q: {Q}")
                

verticals: List = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H"
]
                    
# Breakout of triplets
E: List = [
    ["A", "E", 1],
    ["A", "H", 1],
    ["B", "A", 1],
    ["C", "F", 1],
    ["C", "G", 1],
    ["D", "A", 1],
    ["D", "E", 1],
    ["E", "C", 1],
    ["F", "D", 1],
    ["F", "E", 1],
    ["G", "B", 1],
    ["G", "E", 1],
    ["H", "D", 1],
]

V: List = [0] * len(verticals)

BFS(V, E)
print(V)