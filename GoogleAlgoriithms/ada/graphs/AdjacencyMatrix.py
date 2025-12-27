class Graph:

    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[False] * V for _ in range(V)]


    def add_edge(self, u, v):
        self.adj[u][v] = True
        self.E += 1
