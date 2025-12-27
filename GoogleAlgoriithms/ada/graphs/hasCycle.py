# from collections import defaultdict
# class Graph:

# 	# def __init__(self, vertices = None, graph = None):
# 	# 	if not graph:
# 	# 	    self.graph = defaultdict(list)
# 	# 		self.vertices = 0
# 	# 	else:
# 	# 	    self.graph = graph
# 	# 	    self.vertices = len(graph)

# 	# def add_edge(self,u,v):
# 	# 	self.graph[u].append(v)
# 	# 	self.graph[v].append(u)
	# 	self.vertices += 2

def has_cycle(vertices,graph):
    state = { node : 0 for node in range(vertices)}

    def dfs(node):
        if state[node] == 1: # cycle if find a visited node in current path
            return True

        if state[node] == 2: # no cycle if find a finished node
            return False

        state[node] = 1

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        state[node] = 2 # finish node
        return False


    for node in range(vertices):
        if state[node] == 0:
            if dfs(node):
                return True
    return False

def find_all_cycles(num_nodes, graph):
    visited = set()
    stack = []
    cycles = []

    def dfs(node, current_stack):
        visited.add(node)
        stack.append(node)
        current_stack.add(node)

        for neighbor in graph[node]:
            if neighbor in current_stack:  # Cycle found
                cycle_start_idx = stack.index(neighbor)
                cycles.append(stack[cycle_start_idx:])  # Extract cycle
            elif neighbor not in visited:
                dfs(neighbor, current_stack)

        stack.pop()
        current_stack.remove(node)

    for node in range(num_nodes):
        if node not in visited:
            dfs(node, set())

    # Remove duplicate cycles (sort nodes in each cycle and convert to set)
    unique_cycles = set(tuple(cycle) for cycle in cycles) # remove duplicates
    return [list(cycle) for cycle in unique_cycles]
    # return cycles





graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [1],  # Cycle exists (1 → 2 → 3 → 1)
}

graph2 = {
    0: [1],
    1: [2],
    2: [3],
    3: [],  # Cycle exists (1 → 2 → 3 → 1)
}

# g = Graph()
print(has_cycle(4,graph))
print(has_cycle(4,graph2))
print(find_all_cycles(4,graph))


