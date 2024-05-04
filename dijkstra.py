import sys

class Dijkstra:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def min_distance(self, dist, spt_set):
        # Function to find the vertex with the minimum distance value, from the set of vertices not yet included in the shortest path tree
        min_dist = sys.maxsize
        min_index = 0

        for v in range(self.V):
            if dist[v] < min_dist and not spt_set[v]:
                min_dist = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        # Function to implement Dijkstra's algorithm
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        for _ in range(self.V):
            # Pick the minimum distance vertex from the set of vertices not yet processed
            u = self.min_distance(dist, spt_set)
            # Mark the picked vertex as processed
            spt_set[u] = True

            # Update the distance values of adjacent vertices of the picked vertex
            for v in range(self.V):
                if self.graph[u][v] > 0 and not spt_set[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)

    def print_solution(self, dist):
        # Function to print the final shortest distance from the source vertex to all other vertices
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])


# Example usage
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

# Create object of Dijkstra class
dijkstra_algo = Dijkstra(len(graph))
dijkstra_algo.graph = graph

# Call dijkstra() method with source vertex as argument
dijkstra_algo.dijkstra(0)
