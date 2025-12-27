from collections import defaultdict

class Graph:

	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.vertices = vertices

	def add_edge(self,u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	
	def has_cycle(self):
		state = {i : 0 for i in range(self.vertices) }

		def dfs(node):
			if state[node] == 1:
				return True
			if state[node] == 2:
				return False
			
			state[node] = 1
			for neighbor in self.graph[node]:
				if dfs(neighbor):
					return True
			state[node] = 2
			return False
	

		for node in range(self.vertices):
			if state[node] == 0:
				if dfs(node):
					return True
		return False
	
	
# def detect_cycles(self):
	# 	visited = set()

	# 	def dfs(node, parent):
	# 		visited.add(node)
	# 		for neighbor in self.graph[node]:
	# 			if neighbor not in visited:
	# 				if dfs(neighbor, node):
	# 					return True
	# 			elif neighbor != parent:
	# 				return True
	# 		return False
		
	# 	for vertex in self.graph:
	# 		if vertex not in visited:
	# 			if dfs(vertex, -1):
	# 				return True
	# 	return False