"""
Task: Given a 2D grid where 1 = path and 0 = wall, find the shortest path from (0, 0) to (rows-1, cols-1). Return the path length or -1 if unreachable.
grid = [
    [1, 1, 1],
    [0, 1, 0],
    [0, 1, 1]
] -> 5


grid = [
    [1, 0],
    [0, 1]
]  -> -1

"""
from collections import deque


def find_shortest_path(grid):
    if not grid or grid[0][0] == 0 or grid[-1][-1] == 0:
        return []

    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, [(0, 0)])])

    while queue:
        row, col, curr_path = queue.popleft()
        if row == rows - 1 and col == cols - 1:
            return curr_path

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 0
                queue.append((nr, nc, curr_path + [(nr, nc)]))


    return []



grid1 = [
    [1, 0],
    [0, 1]
]

grid2 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

print(find_shortest_path(grid1))
print(find_shortest_path(grid2))

