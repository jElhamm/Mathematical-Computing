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
            self.graph[u].append(v)                                     # Add v to the adjacency list of u
        else:
            self.graph[u] = [v]                                         # Create a new adjacency list for u with v as the first element

    def bfs(self, start, goal):
        visited = set()                                                 # Keep track of visited vertices
        queue = deque()                                                 # Create a queue for BFS
        queue.append((start, [start]))                                  # Add the start vertex to the queue with its path
        while queue:
            vertex, path = queue.popleft()                              # Dequeue a vertex and its path
            if vertex == goal:                                          # If we have reached the goal vertex
                return path                                             # Return the path from start to goal
            if vertex not in visited:                                   # If the vertex is not visited
                visited.add(vertex)                                     # Mark the vertex as visited
                for neighbor in self.graph.get(vertex, []):             # Iterate over the neighbors of the current vertex
                    queue.append((neighbor, path + [neighbor]))         # Enqueue the neighbor with the extended path
        return None                                                     # If no path from start to goal is found, return None
 

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
 


# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def banner():
    print(
        """
------------------------------------------------------------------------------
|               (:       ***   Welcome   ***       :)                        |
|                                                                            |
|      This program implements a graph data structure and performs           |
|           data analysis using breadth-first search (BFS).                  |
|                                                                            |
|                 For Example:                                               |
|      ---> Enter the number of edges: 5                                     |
|      ---> Enter an edge (space-separated): A B                             |
|      ---> Enter an edge (space-separated): B C                             |
|      ---> Enter an edge (space-separated): C D                             |
|      ---> Enter an edge (space-separated): A E                             |
|      ---> Enter an edge (space-separated): E F                             |
|      ---> Enter the start node: A                                          |
|      ---> Enter the goal node: D                                           |
|      *** Graph Shape: ***                                                  |
|       A -> B                                                               |
|       B -> C                                                               |
|       C -> D                                                               |
|       A -> E                                                               |
|       E -> F                                                               |
|       *** Shortest path: A->B->C->D                                        |
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