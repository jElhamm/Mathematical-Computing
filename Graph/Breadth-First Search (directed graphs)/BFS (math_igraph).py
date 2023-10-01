# This code implements a graph data structure and performs data analysis using Breadth-First Search (BFS).
# This code defines two classes, Graph and DataAnalysis, for analyzing data using a graph. 
#          ---->   You can see the task of each class at the beginning.   <----



import igraph

# The Graph class represents a directed graph.
# Perform a breadth-first search (BFS) to find a path from a start node to a destination node.

class Graph:
    def __init__(self):
        self.graph = igraph.Graph(directed=True)

    def add_edge(self, u, v):
        self.graph.add_edge(u, v)

    def bfs(self, start, goal):
        try:
            path = self.graph.get_shortest_paths(start, goal)[0]
            return path
        except igraph._igraph.InternalError:
            return None
 

# The DataAnalysis class utilizes the Graph class to analyze data by taking user input for the number of edges and
# the edges themselves, and then finding the shortest path between a start node and a goal node.

class DataAnalysis:
    def __init__(self):
        self.graph = Graph()

    def print_graph_shape(self):
        print(" *** Graph Shape: ***")
        for node in self.graph.graph.vs:
            neighbors = self.graph.graph.neighbors(node.index)
            print(f" {node['name']} -> {', '.join(self.graph.graph.vs[neighbors]['name'])}")

    def analyze_data(self):
        n = int(input("---> Enter the number of edges: "))
        for _ in range(n):
            u, v = input("---> Enter an edge (space-separated): ").split()
            self.graph.add_edge(u, v)

        start_node = input("---> Enter the start node: ")
        goal_node = input("---> Enter the goal node: ")
        print("***************************************************************************\n")

        self.print_graph_shape()

        shortest_path = self.graph.bfs(start_node, goal_node)
        if shortest_path:
            print("\n *** Shortest path:", "->".join(self.graph.graph.vs[shortest_path]['name']))
        else:
            print(" (  !  No path found.  !  )")
 