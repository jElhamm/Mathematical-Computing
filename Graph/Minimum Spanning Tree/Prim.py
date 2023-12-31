# The code provided implements Prim's algorithm to find the minimum spanning tree of an undirected weighted graph. 
# The main goal of the code is to analyze graph data and compute the minimum spanning tree using Prim's algorithm.
# The code consists of two classes: 'Graph' and 'DataAnalysis'.



from collections import defaultdict

# The Graph class represents an undirected weighted graph.
# Perform Prim's algorithm to find a minimum spanning tree.

class Graph:
    def __init__(self):
        # Create an empty graph using defaultdict
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        # Add an undirected edge between vertices u and v with the given weight
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim(self):
        visited = set()                                             # Set to keep track of visited vertices
        min_spanning_tree = []                                      # List to store the minimum spanning tree

        start_vertex = next(iter(self.graph))                       # Choose the starting vertex
        visited.add(start_vertex)

        while len(visited) < len(self.graph):
            min_edge = None                                         # Variable to store the minimum weight edge

            for u in visited:
                for v, weight in self.graph[u]:
                    if v not in visited and (min_edge is None or weight < min_edge[2]):
                        min_edge = (u, v, weight)                   # Find the minimum weight edge to an unvisited vertex
            if min_edge is None:
                break

            u, v, weight = min_edge
            min_spanning_tree.append((u, v, weight))                # Add the edge to the minimum spanning tree
            visited.add(v)

        return min_spanning_tree
 

# The DataAnalysis class utilizes the Graph class to analyze data by taking user input for the number of edges and
# the edges themselves, and then finding the minimum spanning tree of the graph.

class DataAnalysis:
    def __init__(self):
        self.graph = Graph()

    def print_graph_shape(self):
        print(" *** Graph Shape: ***")
        for node, edges in self.graph.graph.items():
            for edge in edges:
                v, weight = edge
                print(f"({node}) -[{weight}]-> ({v})")

    def analyze_data(self):
        n = int(input("---> Enter the number of edges: "))
        for _ in range(n):
            u, v, weight = input("---> Enter an edge (space-separated, with weight): ").split()
            weight = int(weight)
            self.graph.add_edge(u, v, weight)

        print("***************************************************************************\n")
        self.print_graph_shape()

        min_spanning_tree = self.graph.prim()
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
|           data analysis using Prim's algorithm for minimum                 |
|               spanning tree on an undirected weighted graph.               |
|                                                                            |
|                 For Example:                                               |
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
|      (B) -[4]-> (C)                                                        |
|      (C) -[3]-> (D)                                                        |
|      (D) -[2]-> (E)                                                        |
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