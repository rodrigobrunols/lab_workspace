from collections import deque

def find_islands(grid):
    """Finds all islands using DFS and labels them uniquely."""
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    islands = {}
    island_id = 0
    
    def dfs(x, y, island_id):
        """Perform DFS to mark all cells of the island."""
        if x < 0 or x >= rows or y < 0 or y >= cols or visited[x][y] or grid[x][y] == 0:
            return
        visited[x][y] = True
        islands[island_id].append((x, y))
        
        # Explore in 4 directions (Up, Down, Left, Right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(x + dx, y + dy, island_id)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                islands[island_id] = []
                dfs(r, c, island_id)
                island_id += 1  # Move to next island ID

    return islands

def find_bridges(grid, islands):
    """Finds the shortest bridges between islands."""
    rows, cols = len(grid), len(grid[0])
    edges = []
    
    def search_bridge(island_id, x, y, dx, dy):
        """Finds the shortest bridge from an island in one direction."""
        distance = 0
        while 0 <= x < rows and 0 <= y < cols:
            if grid[x][y] == 1:
                # Found another island
                for id, positions in islands.items():
                    if (x, y) in positions and id != island_id:
                        return (distance, island_id, id)
            x += dx
            y += dy
            distance += 1
        return None

    for island_id, positions in islands.items():
        for x, y in positions:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
                bridge = search_bridge(island_id, x + dx, y + dy, dx, dy)
                if bridge:
                    edges.append(bridge)
    
    return edges

def find_minimum_spanning_tree(edges, num_islands):
    """Applies Kruskal's Algorithm to find the minimum spanning tree."""
    edges.sort()  # Sort by distance
    parent = {i: i for i in range(num_islands)}
    
    def find(x):
        """Finds the root of a node (with path compression)."""
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        """Unites two sets."""
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_y] = root_x
            return True
        return False

    mst = []
    for distance, u, v in edges:
        if union(u, v):
            mst.append((u, v, distance))

    return mst

def connect_islands(grid):
    """Full pipeline to find minimum bridges to connect all islands."""
    islands = find_islands(grid)
    print("Identified Islands:", islands)

    edges = find_bridges(grid, islands)
    print("Possible Bridges:", edges)

    mst = find_minimum_spanning_tree(edges, len(islands))
    print("Minimum Bridges Required:", mst)
    return mst

# Example grid
grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1]
]

connect_islands(grid)