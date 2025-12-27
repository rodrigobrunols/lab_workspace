from collections import defaultdict
class Graph:

	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.vertices = vertices

	def add_edge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def has_cycle(self, vertices):
		state = { node : 0 for node in range(vertices)}

		def dfs(node):
			if state[node] == 1:
				return True

			if state[node] == 2:
				return False

			state[node] = 1

			for neighbor in graph[node]:
				if dfs(neighbor):
					return True
			state[node] = 2
			return False


		for node in range(vertices):
			if state[node] == 0:
				if dfs(node):
					return True
		return False


"""
graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [1],  # Cycle exists (1 → 2 → 3 → 1)
}
"""