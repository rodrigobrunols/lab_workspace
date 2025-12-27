class Graph:

    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
        self.weight = [[] for _ in range(V)]

    def addEdge(self, u, v, w=1):
        self.adj[u].append(v)
        self.weight[u].append(w)
        self.E += 1

    def print(self):
        for u in range(len(self.adj)):
            print(u, self.adj[u], end=", ")
            print(self.weight[u])

    def dfs(self, node, visited=None ):
        if not visited:
            visited = set()
        if node not in visited:
            visited.add(node)
            for neigh in self.adj[node]:
                self.dfs(neigh,visited)

    def dfsVisitedList(self, node, visited = set()):
        if node and  node in visited:
            return []

        visited.add(node)
        listOfVisitedNodes = [node]

        for neigh in self.adj[node]:
            listOfVisitedNodes += self.dfsVisitedList(neigh, visited)

        return listOfVisitedNodes



g = Graph(6) # ignoring the 0 node
g.addEdge(1, 2)
g.addEdge(2, 1)
g.addEdge(1, 4)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 2)
g.addEdge(2, 4)
g.addEdge(4, 2)
g.addEdge(2, 5)
g.addEdge(5, 2)
g.addEdge(3, 5)
g.addEdge(5, 3)
g.addEdge(4, 5)
g.addEdge(5, 4)
print( g.dfsVisitedList(1))

# test = []
# for i in range(5):
#     test += [i]
# print(test)
# traversal = []
# graph.dfs(1,traversal,set())
# print(traversal)

