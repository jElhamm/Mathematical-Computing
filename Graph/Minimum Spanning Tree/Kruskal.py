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
 

# The DisjointSet class represents a disjoint-set data structure.
# Used in Kruskal's algorithm to keep track of connected components.

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        for v in vertices:
            self.parent[v] = v

    # Find the parent of a vertex (with path compression)
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    # Union two subsets by setting the parent of one vertex to the other vertex
    def union(self, v1, v2):
        self.parent[self.find(v1)] = self.find(v2)
 


# The DataAnalysis class utilizes the Graph and DisjointSet classes to analyze data by taking user input for the
# number of vertices, the number of edges, and the edges themselves, and then finding the minimum spanning tree of the graph.

class DataAnalysis:
    def __init__(self):
        self.graph = None

    def print_graph_shape(self):
        print(" *** Graph Shape: ***")
        for u, v, weight in self.graph.edges:
            print(f"({u}) -[{weight}]-> ({v})")

    def analyze_data(self):
        n = int(input("---> Enter the number of vertices: "))
        self.graph = Graph(n)

        m = int(input("---> Enter the number of edges: "))
        for _ in range(m):
            u, v, weight = input("---> Enter an edge (space-separated, with weight): ").split()
            weight = int(weight)
            self.graph.add_edge(u, v, weight)

        print("***************************************************************************\n")
        self.print_graph_shape()

        min_spanning_tree = self.graph.kruskal()
        print("\n *** Minimum Spanning Tree ***")
        for u, v, weight in min_spanning_tree:
            print(f"({u}) -[{weight}]-> ({v})")
 
 

# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def banner():
    print("""
          
------------------------------------------------------------------------------
|               (:       ***   Welcome   ***       :)                        |
|                                                                            |
|      This program implements a graph data structure and performs           |
|           data analysis using Kruskal's algorithm for minimum              |
|                        spanning tree on an undirected weighted graph.      |
|                                                                            |
|                 For Example:                                               |
|      ---> Enter the number of vertices: 6                                  |
|      ---> Enter the number of edges: 6                                     |
|      ---> Enter an edge (space-separated, with weight): A B 1              |
|      ---> Enter an edge (space-separated, with weight): B C 4              |
|      ---> Enter an edge (space-separated, with weight): C D 3              |
|      ---> Enter an edge (space-separated, with weight): D E 2              |
|      ---> Enter an edge (space-separated, with weight): E F 5              |
|      ---> Enter an edge (space-separated, with weight): F A 6              |
|      *** Graph Shape: ***                                                  |
|      (A) -[1]-> (B)                                                        |
|      (B) -[4]-> (C)                                                        |
|      (C) -[3]-> (D)                                                        |
|      (D) -[2]-> (E)                                                        |
|      (E) -[5]-> (F)                                                        |
|      (F) -[6]-> (A)                                                        |
|                                                                            |
|       *** Minimum Spanning Tree ***                                        |
|      (A) -[1]-> (B)                                                        |
|      (D) -[2]-> (E)                                                        |
|      (C) -[3]-> (D)                                                        |
|      (B) -[4]-> (C)                                                        |
|      (E) -[5]-> (F)                                                        |
|                                                                            |
------------------------------------------------------------------------------
        """)

def main():
    banner()
    data_analysis = DataAnalysis()
    data_analysis.analyze_data()
    print("***************************************************************************\n")

if __name__ == "__main__":
    main()


# An example of how to use the program is shown.