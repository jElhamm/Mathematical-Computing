# This code implements a graph data structure and performs data analysis using depth-first search (DFS).
# This code defines two classes, Graph and DataAnalysis, for analyzing data using a graph. 
#          ---->   You can see the task of each class at the beginning.   <----


# The Graph class represents a directed graph.
# Perform a depth first search (DFS) to find a path from a start node to a destination node.

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)                                         # Add v to the adjacency list of u
        else:
            self.graph[u] = [v]                                             # Create a new adjacency list for u with v as the first element

    def dfs(self, start, goal):
        visited = set()                                                     # Keep track of visited vertices
        path = []                                                           # Store the path from start to goal
        self._dfs_util(start, goal, visited, path)
        return path

    def _dfs_util(self, vertex, goal, visited, path):
        visited.add(vertex)                                                 # Mark the vertex as visited
        path.append(vertex)                                                 # Add the vertex to the current path

        if vertex == goal:                                                  # If we have reached the goal vertex
            return True

        for neighbor in self.graph.get(vertex, []):                         # Iterate over the neighbors of the current vertex
            if neighbor not in visited:                                     # If the neighbor is not visited
                if self._dfs_util(neighbor, goal, visited, path):           # Recursively call DFS on the neighbor
                    return True                                             # If the neighbor reaches the goal, return True

        path.pop()                                                          # If no path from vertex leads to the goal, remove the vertex from the path
        return False
 