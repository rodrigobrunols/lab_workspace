from collections import deque, defaultdict


def find_all_paths(graph):
    stack = [(0, [0])]
    paths = []
    while stack:
        node, path = stack.pop()
        if node == len(graph) - 1:
            paths.append(path)
        for neighbor in graph[node]:
            stack.append((neighbor, path + [neighbor]))
    return paths


def main():
    graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }

    graph2 = {
        0: [1],
        1: [2],
        2: [3],
        3: []
    }

    graph3 = {
        0: [1, 2],
        1: [],
        2: []
    }

    print(find_all_paths(graph))
    print(find_all_paths(graph2))
    print(find_all_paths(graph3))




if __name__ == "__main__":
    main()
