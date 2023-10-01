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
 