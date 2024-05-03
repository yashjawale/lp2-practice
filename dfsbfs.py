from collections import defaultdict

class Graph:
    def __init__(self):
        # Initialize a defaultdict to store the graph
        # The keys are the vertices and the values are lists of adjacent vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Function to add an edge between vertices u and v
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        # Utility function for Depth First Search traversal
        # v: current vertex being visited
        # visited: list to keep track of visited vertices
        visited[v] = True
        # Print the current vertex
        print(v, end=' ')
        # Recursively visit all adjacent vertices of v
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, v):
        # Depth First Search traversal starting from vertex v
        visited = [False] * len(self.graph)
        # Call the utility function to perform DFS
        self.dfs_util(v, visited)

    def bfs(self, s):
        # Breadth First Search traversal starting from vertex s
        visited = [False] * len(self.graph)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue a vertex from the queue
            s = queue.pop(0)
            # Print the dequeued vertex
            print(s, end=' ')

            # Enqueue all adjacent vertices of the dequeued vertex
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth First Traversal (starting from vertex 2):")
g.dfs(2)
print("\nBreadth First Traversal (starting from vertex 2):")
g.bfs(2)
