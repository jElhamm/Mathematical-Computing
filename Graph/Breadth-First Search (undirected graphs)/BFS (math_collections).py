# This code implements a graph data structure and performs data analysis using Breadth-First Search (BFS).
# This code defines two classes, Graph and DataAnalysis, for analyzing data using a graph. 
#          ---->   You can see the task of each class at the beginning.   <----



from collections import deque

# The Graph class represents a directed graph.
# Perform a breadth-first search (BFS) to find a path from a start node to a destination node.

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)                                     # Add v to the list of neighbors for u
        else:
            self.graph[u] = [v]                                         # Initialize the list of neighbors for u with v

        if v in self.graph:                                             # Add this block to support undirected graph
            self.graph[v].append(u)                                     # Add u to the list of neighbors for v
        else:
            self.graph[v] = [u]                                         # Initialize the list of neighbors for v with u

    def bfs(self, start, goal):
        visited = set()
        queue = deque()
        queue.append((start, [start]))                                  # Start with the start node and a path containing only the start node
        while queue:
            vertex, path = queue.popleft()                              # Get the first node and its path from the queue
            if vertex == goal:                                          # If the goal node is reached, return the path
                return path

            if vertex not in visited:                                   # If the node has not been visited yet
                visited.add(vertex)                                     # Mark the node as visited
                for neighbor in self.graph.get(vertex, []):             # Explore all neighbors of the current node
                    queue.append((neighbor, path + [neighbor]))         # Add each neighbor to the queue with an extended path

        return None
 

# The DataAnalysis class utilizes the Graph class to analyze data by taking user input for the number of edges and
# the edges themselves, and then finding the shortest path between a start node and a goal node.

class DataAnalysis:
    def __init__(self):
        self.graph = Graph()

    def print_graph_shape(self):
        print(" *** Graph Shape: ***")
        for node, neighbors in self.graph.graph.items():
            print(f" {node} -> {', '.join(neighbors)}")

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
            print("\n *** Shortest path:", "->".join(shortest_path))
        else:
            print(" (  !  No path found.  !  )")
 