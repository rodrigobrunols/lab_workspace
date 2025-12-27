import collections
from typing import List


from collections import deque

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:

        # build graph
        graph = collections.defaultdict(list)
        inDegree = [0] * n

        for a, b in relations:
            graph[a].append(b)
            inDegree[b] += 1

        queue = deque([i for i in range(1, n + 1) if inDegree[i] == 0])
        semester = 0
        coursesTaken = 0

        while queue:
            semester += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                coursesTaken += 1

                for neighbor in graph[course]:
                    inDegree[neighbor] -= 1
                    if inDegree[neighbor] == 0:
                        queue.append(neighbor)

        return semester if coursesTaken == n else -1






