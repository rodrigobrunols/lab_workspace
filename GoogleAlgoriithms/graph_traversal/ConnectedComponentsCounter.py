
from collections import defaultdict, deque


# def count_components_dfs_iterative(graph):
#     visited = set()
#     count = 0
#
#     for node in graph:
#         if node not in visited:
#             stack = [node]
#             visited.add(node)  # Mark as visited when pushed
#             while stack:
#                 current = stack.pop()
#                 for neighbor in graph[current]:
#                     if neighbor not in visited:
#                         visited.add(neighbor)
#                         stack.append(neighbor)
#             count += 1  # End of component
#     return count

def count_components_dfs_iterative(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            stack = deque([node])
            visited.add(node)
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

            count += 1

    return count


def count_components_dfs_recursive(graph):
    visited = set()
    count = 0

    def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1
    return count


graph_1 = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3],
    5: []
}

graph_2 = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: []
}

graph_3 = {
    0: [],
    1: []
}

print(count_components_dfs_iterative(graph_1))
print(count_components_dfs_iterative(graph_2))
print(count_components_dfs_iterative(graph_3))

print(count_components_dfs_recursive(graph_1))
print(count_components_dfs_recursive(graph_2))
print(count_components_dfs_recursive(graph_3))
