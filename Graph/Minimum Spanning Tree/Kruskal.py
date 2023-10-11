# The code provided implements Kruskal's algorithm to find the minimum spanning tree of an undirected weighted graph.
# The main goal of the code is to analyze graph data and compute the minimum spanning tree using Kruskal's algorithm.



# The Graph class represents an undirected weighted graph.
# Perform Kruskal's algorithm to find a minimum spanning tree.

class Graph:
    def __init__(self, vertices):
        # Create a graph with the given number of vertices
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        # Add an undirected edge between vertices u and v with the given weight
        self.edges.append((u, v, weight))

    def find(self, parent, i):
        # Find the parent of a vertex (with path compression)
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        # Union two subsets based on rank (union by rank)
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        result = []                                     # List to store the minimum spanning tree
        self.edges.sort(key=lambda x: x[2])             # Sort edges in ascending order of weights
        parent = []
        rank = []

        for v in range(self.V):
            parent.append(v)
            rank.append(0)

        i = 0
        e = 0                                          # Index variable to iterate over edges
        while e < self.V - 1:
            u, v, weight = self.edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append((u, v, weight))
                self.union(parent, rank, x, y)

        return result
 