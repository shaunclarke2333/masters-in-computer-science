def BFS(V, E):
    for i in range(len(V)):
        V[i] = -1           # all vertices not visited
    count = 0
    for i in range(len(V)):   # for all possible sources
        if (V[i] == -1):
            Q = [i]           # enqueue the source
            V[i], count = count, count + 1   # visit it
            while (len(Q) != 0):             # for all enqueued
                for e in E:                  # search neighbors
                    if (e[0] == Q[0]) and (V[e[1]] == -1):
                        Q.append(e[1])       # enqueue it
                        V[e[1]], count = count, count + 1   # visit it
                Q.pop(0)                     # dequeue it

V = [0] * 8

E = [
    [0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 4, 1],
    [3, 6, 1], [4, 5, 1], [4, 7, 1], [5, 8, 1], [7, 8, 1]
]

BFS(V, E)
print(V)
