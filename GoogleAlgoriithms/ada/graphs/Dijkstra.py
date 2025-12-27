import heapq
from typing import List, Tuple

def dijkstra(graph: List[List[Tuple[int, int]]], start: int) -> List[float]:
    # initialize

    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        # skip if alread found a shortest path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            dist = current_distance + weight
            # check small path
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))

    return distances


# Graph represented as an adjacency list
# Node 0 -> [(1, 4), (2, 1)]
# Node 1 -> [(3, 1)]
# Node 2 -> [(1, 2), (3, 5)]
# Node 3 -> []
graph = [
    [(1, 4), (2, 1)],  # Neighbors of node 0
    [(3, 1)],          # Neighbors of node 1
    [(1, 2), (3, 5)],  # Neighbors of node 2
    []                 # Neighbors of node 3
]

start_node = 0
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances:", shortest_distances)
