from typing import List

# This function creates a new list with the names of the current vertices in the queue
def current_vertices(Q: List, verticals: List) -> List:
    # List to hold vertices names
    vertices_names: List = []
    for q in Q:
        # Adding vertices to list
        vertices_names.append(verticals[q])
    return vertices_names

def DFS(V, E):
    def __visit(i, count):
#         print(f"This is i: {i}, this is count: {count}")
#         print(f"V[i] = {count}, count = {count+1}")
        print(f"DFS called for vertex {verticals[i]}")
        V[i], count = count, count+1
        print(f"Vertex {verticals[i]} visited and received the stamp {V[i]}, current array: {V}")
        for e in E:
#             print(f"if e[0]:{e[0]} == i:{i} and V[e[1]]:{V[e[1]]} == -1")
            if (e[0] == i) and (V[e[1]] == -1):
#                 print(f"count = __visit(e[1]:{e[1]}, count:{count})")
                count = __visit(e[1], count)
                
                
#         print(f"This is count: {count}")     
        return count
        

    for i in range(len(V)):
        V[i] = -1
    count = 0
    for i in range(len(V)):
#         print(f"if (V[i]:{V[i]} == -1):")
        if (V[i] == -1):
#             print(f"count = __visit(i, count)")
            count = __visit(i, count)
            
            
# adjacency list
adjacency_list: List = [
    ["E", "H"], # A
    ["A"], # B
    ["F", "G"], # C
    ["A", "E"], # D
    ["C"], # E
    ["D", "E"], # F
    ["B", "E"], # G
    ["D"] # H
]              

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
                    


V: List = [0] * len(verticals)

# Breakout of triplets
E: List = [
    [0, 4, 1],
    [0, 7, 1],
    [1, 0, 1],
    [2, 5, 1],
    [2, 6, 1],
    [3, 0, 1],
    [3, 4, 1],
    [4, 2, 1],
    [5, 3, 1],
    [5, 4, 1],
    [6, 1, 1],
    [6, 4, 1],
    [7, 3, 1],
]
DFS(V, E)
print(V)
