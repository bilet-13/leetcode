class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs: start from 1 cell and mark the land cell to water
        # use a global var to store the number of islands

        num_islands = 0
        n = len(grid)
        m = len(grid[0])

        def dfs(s_x, s_y):
            stack = [(s_x, s_y)]
            grid[s_x][s_y] = "0"

            while stack:
                x, y = stack.pop()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx = x + dx
                    ny = y + dy

                    if n > nx >= 0 and m > ny >= 0 and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        stack.append((nx, ny))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)

        return num_islands

        