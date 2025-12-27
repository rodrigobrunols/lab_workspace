from heapq import heappush, heappop


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    previous_nodes = {node: None for node in graph}

    priority_queue = [(0, start)]

    while priority_queue:
        # print( heappop(priority_queue))
        current_distance, current_node = heappop(priority_queue)


        if current_distance > distances[current_node]:
            continue

        # print(f"current_node-> {graph[current_node].items()}")
        for neigh, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neigh]:
                distances[neigh] = distance
                previous_nodes[neigh] = current_node
                heappush(priority_queue, (distance, neigh))


    print(distances)
    print(previous_nodes)
    current = end

    path = []
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    print(f"path: ", path)
    return distances[end], path if path[-1] == end else None

    # print(f"A menor distancia entre {start} e {end} é: {distances[end]}")
    # print(f"Path = {'->'.join(path)}")


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
end_node = 'D'

distance, path = dijkstra(graph, start_node, end_node)
print(f"Shortest distance from {start_node} to {end_node}: {distance}")
print(f"Optimal path: {' -> '.join(path)}")
# print(f"Optimal path: {' -> '.join(path)}")

# def dijkstra(graph, start, end):
#     """
#     Find the shortest path between two nodes in a weighted graph using Dijkstra's algorithm.
#
#     Args:
#         graph: Dictionary representing the graph {node: {neighbor: weight}}
#         start: Starting node
#         end: Destination node
#
#     Returns:
#         tuple: (shortest distance, path as list of nodes)
#     """
#     # Initialize distances with infinity and set start to 0
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#
#     # Priority queue: (distance, node)
#     priority_queue = [(0, start)]
#
#     # To keep track of the path
#     previous_nodes = {node: None for node in graph}
#
#     while priority_queue:
#         current_distance, current_node = heapq.heappop(priority_queue)
#
#         # Skip if we've already found a better path
#         if current_distance > distances[current_node]:
#             continue
#
#         # Explore neighbors
#         for neighbor, weight in graph[current_node].items():
#             distance = current_distance + weight
#
#             # Only consider this new path if it's better
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 previous_nodes[neighbor] = current_node
#                 heapq.heappush(priority_queue, (distance, neighbor))
#
#     # Reconstruct the path
#     path = []
#     current = end
#     while current is not None:
#         path.append(current)
#         current = previous_nodes[current]
#     path.reverse()  # Reverse to get start -> end
#
#     return distances[end], path if path[0] == end else None
#
# # Example usage
#
#
# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }
#
# start_node = 'A'
# end_node = 'D'
#
# distance, path = dijkstra(graph, start_node, end_node)
# print(f"Shortest distance from {start_node} to {end_node}: {distance}")
# print(f"Optimal path: {' -> '.join(path)}")
#
