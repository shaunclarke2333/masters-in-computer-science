"""
Author: Shaun Clarke
Class: CSC6023 Advanced Algorithms
Module: Module 7 – Graphs (Dijkstra)
Assignment (Final Update):
    - Use the slide's Dijkstra code verbatim.
    - Use an adjacency MATRIX LITERAL exactly like the slide example (no builder method).
    - Print readable journeys: Shire ➜ Rivendell, then Rivendell ➜ Mt. Doom.
"""
import sys
from typing import List, Tuple

# === Dijkstra code copied from slides (word-for-word) ===
class Graph():
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.paths = [[] for _ in range(self.V)]
        
    def printSolution(self, dist):
        print("Vertex \tDistance from Source \tPath")
        for node in range(self.V):
            print(node, "\t", dist[node], "\t\t", self.paths[node])

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        self.paths[src] = [src]

        for _ in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True

            for y in range(self.V):
                if self.graph[x][y] > 0 and not sptSet[y] and \
                   dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = self.graph[x][y] + dist[x]
                    self.paths[y] = self.paths[x] + [y]

        self.printSolution(dist)
        return dist


def describe_path(names: List[str], matrix: List[List[int]], path: List[int]) -> Tuple[str, int]:
    if not path or len(path) == 1:
        return (f"Already at {names[path[0]]}" if path else "No path found."), 0
    steps, total = [], 0
    for i in range(len(path) - 1):
        a, b = path[i], path[i+1]
        w = matrix[a][b]
        total += w
        steps.append(f"{names[a]} ➜ {names[b]} ({w})")
    return " then ".join(steps), total


def main():
    names = ["Shire","Bree","Rivendell","Moria","Dale","Lorien","Isengard","Edoras","Minas Tirith","Emyn Muil","Mt. Doom"]

    # === ADJACENCY MATRIX LITERAL (from the map image) ===
    matrix = [
        [0, 131, 0, 0, 0, 0, 481, 0, 0, 0, 0],
        [131, 0, 306, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 306, 0, 178, 362, 0, 0, 0, 0, 0, 0],
        [0, 0, 178, 0, 0, 172, 173, 0, 0, 0, 0],
        [0, 0, 362, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 172, 0, 0, 0, 201, 0, 217, 0],
        [481, 0, 0, 173, 0, 0, 0, 174, 0, 0, 0],
        [0, 0, 0, 0, 0, 201, 174, 0, 315, 262, 0],
        [0, 0, 0, 0, 0, 0, 0, 315, 0, 264, 178],
        [0, 0, 0, 0, 0, 217, 0, 262, 264, 0, 183],
        [0, 0, 0, 0, 0, 0, 0, 0, 178, 183, 0]
    ]

    # Run 1: from Shire (0)
    g1 = Graph(len(matrix))
    g1.graph = matrix
    print("Dijkstra from Shire 0")
    g1.dijkstra(0)

    # Run 2: from Rivendell (2)
    g2 = Graph(len(matrix))
    g2.graph = matrix
    print("\nDijkstra from Rivendell 2")
    g2.dijkstra(2)

    # Human readable narrative
    shire_to_riv = g1.paths[2]
    riv_to_doom  = g2.paths[10]

    s1, t1 = describe_path(names, matrix, shire_to_riv)
    s2, t2 = describe_path(names, matrix, riv_to_doom)

    print(f"Frodo should go first to Rivendell: {s1}. Distance = {t1}")
    print(f"From Rivendell, Frodo should continue to Mt. Doom: {s2}. Distance = {t2}")
    print(f"Total journey distance: {t1 + t2}")


if __name__ == "__main__":
    main()
