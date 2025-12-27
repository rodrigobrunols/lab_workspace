import heapq
from collections import defaultdict

def prim_mst(graph, start=0):
    mst_edges = []
    total_weight = 0
    visited = set()
    min_heap = [(0,start, -1)]

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)

        if current in visited:
            continue

        visited.add(current)
        total_weight += weight
        if  parent != -1:
            mst_edges.append((parent,current,weight))

        for neighbor, w in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w,neighbor,current))

    return total_weight, mst_edges




# Example Usage:
graph = {
    0: [(1, 1), (2, 3)],
    1: [(0, 1), (2, 3), (3, 6)],
    2: [(0, 3), (1, 3), (3, 4), (4, 2)],
    3: [(1, 6), (2, 4), (4, 5)],
    4: [(2, 2), (3, 5)]
}

total_weight, mst_edges = prim_mst(graph)
print("Prim's MST Total Weight:", total_weight)
print("Prim's MST Edges:", mst_edges)
