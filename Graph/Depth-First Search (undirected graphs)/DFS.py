# This code implements a graph data structure and performs data analysis using depth-first search (DFS).
# This code defines two classes, Graph and DataAnalysis, for analyzing data using a graph. 
#          ---->   You can see the task of each class at the beginning.   <----


# The Graph class represents an undirected graph and provides methods for adding edges 
# and performing depth-first search (DFS) to find a path from a start node  to a goal node. 

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)                                     # Add v to the adjacency list of u
        else:
            self.graph[u] = [v]                                         # Create a new adjacency list for u with v as the first element

        if v in self.graph:
            self.graph[v].append(u)                                     # Add u to the adjacency list of v
        else:
            self.graph[v] = [u]                                         # Create a new adjacency list for v with u as the first element

    def dfs(self, start, goal):
        visited = set()                                                 # Keep track of visited vertices
        path = []                                                       # Store the path from start to goal
        self._dfs_util(start, goal, visited, path)
        return path

    def _dfs_util(self, vertex, goal, visited, path):
        visited.add(vertex)                                             # Mark the vertex as visited
        path.append(vertex)                                             # Add the vertex to the current path

        if vertex == goal:                                              # If we have reached the goal vertex
            return True

        for neighbor in self.graph[vertex]:                             # Iterate over the neighbors of the current vertex
            if neighbor not in visited:                                 # If the neighbor is not visited
                if self._dfs_util(neighbor, goal, visited, path):       # Recursively call DFS on the neighbor
                    return True                                         # If the neighbor reaches the goal, return True

        path.pop()                                                  # If no path from vertex leads to the goal, remove the vertex from the path
        return False
 

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

        shortest_path = self.graph.dfs(start_node, goal_node)
        if shortest_path:
            print("\n *** Shortest path:", "->".join(shortest_path))
        else:
            print(" (  !  No path found.  !  )")
 