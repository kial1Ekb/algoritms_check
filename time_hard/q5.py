"""
Разработайте программу, которая оценивает пространственную сложность алгоритма поиска кратчайшего пути в графе с
использованием алгоритма Дейкстры. Программа должна генерировать случайный граф, находить кратчайший путь от начальной
вершины до остальных и измерять объем используемой памяти.
"""

import random
import sys
import tracemalloc

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.min_distance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        return dist

    def min_distance(self, dist, sptSet):
        min = sys.maxsize
        min_index = 0
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

def generate_random_graph(v, e):
    g = Graph(v)
    for _ in range(e):
        u = random.randint(0, v-1)
        v = random.randint(0, v-1)
        w = random.randint(1, 10)
        g.add_edge(u, v, w)
    return g

def measure_memory_usage(g, src):
    tracemalloc.start()
    distances = g.dijkstra(src)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Кратчайшие пути от вершины {src} до остальных: {distances}")
    print(f"Текущее использование памяти: {current / 1024:.2f} KB")
    print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")

def main():
    vertices = int(input("Введите количество вершин в графе: "))
    edges = int(input("Введите количество рёбер в графе: "))
    source_vertex = int(input("Введите начальную вершину для алгоритма Дейкстры: "))
    g = generate_random_graph(vertices, edges)
    measure_memory_usage(g, source_vertex)

if __name__ == "__main__":
    main()
