import heapq
from collections import deque
from typing import List

class Solution:
    def minBridgesToConnectIslands(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        island_id = 2  # Start from 2 to avoid confusion with water (0) and land (1)
        island_cells = {}

        # Step 1: Identify all islands using DFS and label them uniquely
        def dfs(x, y, island_id):
            """Perform DFS to label an island and collect its cells."""
            stack = [(x, y)]
            grid[x][y] = island_id
            island_cells[island_id].append((x, y))

            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1:
                        grid[nr][nc] = island_id
                        island_cells[island_id].append((nr, nc))
                        stack.append((nr, nc))

        # Label islands using DFS
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    island_cells[island_id] = []
                    dfs(r, c, island_id)
                    island_id += 1

        total_islands = island_id - 2  # Since IDs started at 2

        # Step 2: Find shortest bridges using BFS
        graph = {i: [] for i in range(2, island_id)}

        def bfs_find_bridges(island_id, start_cells):
            """Perform BFS to find the shortest bridges to other islands."""
            queue = deque([(x, y, 0) for x, y in start_cells])  # (x, y, distance)
            visited = set(start_cells)

            while queue:
                x, y, dist = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                        if grid[nx][ny] == 0:  # Water, expand search
                            queue.append((nx, ny, dist + 1))
                            visited.add((nx, ny))
                        elif grid[nx][ny] > 1 and grid[nx][ny] != island_id:  # Found another island
                            graph[island_id].append((grid[nx][ny], dist))
                            graph[grid[nx][ny]].append((island_id, dist))

        # Compute shortest bridges using BFS
        for island_id, positions in island_cells.items():
            bfs_find_bridges(island_id, positions)

        # Step 3: Use Prim’s Algorithm to find the MST (minimum bridges needed)
        def prim():
            """Use Prim’s algorithm to find the minimum spanning tree."""
            min_heap = [(0, 2)]  # (cost, island_id), start from the first island
            visited = set()
            mst_cost = 0
            edges_used = 0

            while min_heap and len(visited) < total_islands:
                weight, u = heapq.heappop(min_heap)
                if u in visited:
                    continue
                visited.add(u)
                mst_cost += weight
                edges_used += 1

                for v, cost in graph[u]:
                    if v not in visited:
                        heapq.heappush(min_heap, (cost, v))

            return mst_cost if edges_used == total_islands else -1  # Ensure all islands are connected

        return prim()


# Example grid
grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1]
]

solution = Solution()
print(solution.minBridgesToConnectIslands(grid))  # Expected output: shortest number of bridges needed
