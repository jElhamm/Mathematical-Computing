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
 