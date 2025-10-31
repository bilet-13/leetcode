class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # time complexity o(nm) o(v + E) = o(V + 4V) = o(nm)
        m = len(heights)
        n = len(heights[0])

        def BFS(record_grid, start_points):
            queue = deque(start_points)

            while queue:
                x, y = queue.popleft()

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx = x + dx
                    ny = y + dy

                    if m > nx >= 0 and n > ny >= 0 and not record_grid[nx][ny] and heights[x][y] <= heights[nx][ny]:
                        record_grid[nx][ny] = True
                        queue.append((nx, ny))
            return

        atl_cells = [(i, j) for i in range(m) for j in range(n) if i == m - 1 or j == n - 1]
        pac_cells = [(i, j) for i in range(m) for j in range(n) if i == 0  or j == 0]

        atl_grid  = [[ True if i == m - 1 or j == n - 1 else False for j in range(n)] for i in range(m)]
        pac_grid = [[ True if i == 0 or j == 0 else False for j in range(n)] for i in range(m)]

        BFS(atl_grid, atl_cells)
        BFS(pac_grid, pac_cells)

        return [[i, j] for i in range(m) for j in range(n) if atl_grid[i][j] and pac_grid[i][j]]
        