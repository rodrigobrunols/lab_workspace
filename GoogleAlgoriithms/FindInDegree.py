from collections import defaultdict


def find_in_degree(edges, n):
    in_degree = [0] * n
    for u, v in edges:
        in_degree[v] += 1
    return in_degree


def find_in_degree_in_adj_list(adj_list, n):
    in_degree = [0] * n

    for i, list_ in adj_list.items():
        print(i, list_)
        for v in list_:
            in_degree[v] += 1

    return in_degree



edges_1 = [(0, 1), (1, 2), (1, 3), (3, 2), (3, 4)]
adj_list_1 = {0: [1], 1: [2, 3], 2: [], 3: [2, 4], 4: []}

print(find_in_degree(edges_1, 5))
print(find_in_degree_in_adj_list(adj_list_1, 5))
# print(365 ** 1.01)


