class Solution:
    def BFS(self, grid, root):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = [root]

        while queue:
            x, y = queue.pop(0)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    queue.append((nx, ny))


    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1

                    self.BFS(grid,(i, j))


        return islands
