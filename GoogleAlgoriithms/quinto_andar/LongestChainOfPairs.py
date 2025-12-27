"""
Given a list of pairs [ (a, b), (b, c), (c, d), (x, y), (y, z) ],
find the longest chain of connected pairs and return it as a sequence.

Example:
Input: [ ["a", "b"], ["b", "c"], ["c", "d"], ["x", "y"], ["y", "z"] ]
Output: "a->b->c->d" (or "x->y->z", since both have the same length)


Challenge:
If multiple chains have the same length, return the lexicographically smaller one.
Handle cycles (e.g., [ ["a", "b"], ["b", "a"] ] should return "a->b" or detect the cycle).
"""


from collections import defaultdict, deque


def longest_chain(pairs):
    if not pairs:
        return ""


    graph = defaultdict(list)
    in_degree = defaultdict(int)
    nodes = set()

    for u, v in pairs:
        graph[u].append(v)
        in_degree[v] += 1
        nodes.add(u)
        nodes.add(v)


    starts = [n for n in nodes if in_degree[n] == 0]
    if not starts:
        starts = [min(nodes)]

    longest_path = []
    for start in sorted(starts):
        stack = [(start, [start])]

        while stack:
            node, path = stack.pop()
            # update longest
            if len(path) > len(longest_path):
                longest_path = path
            elif len(path) == len(longest_path) and path < longest_path:
                longest_path = path

            # Explore neighbors in reverse order to process lex order
            for neighbor in sorted(graph[node], reverse=True):
                path.append(neighbor)
                stack.append((neighbor, path))

    return "->".join(longest_path)



print(longest_chain([["a","b"], ["b","c"], ["c","d"], ["x","y"], ["y","z"]]))
# Output: "a->b->c->d"


print(longest_chain([["a","b"], ["b","a"], ["c","d"]]))
# Output: "a->b" (or "c->d" if we want the lex smaller chain)
