class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
          # use dfs to find areas of each island and update the global var max_area
        # time complexity o(n * m) n = len(grid) m= len(grid[0])
        max_area = 0
        n = len(grid)
        m = len(grid[0])

        def get_area(start_x, start_y):
            # dfs
            area = 0
            stack = [(start_x, start_y)]
            grid[start_x][start_y] = 0

            while stack:
                x, y = stack.pop()
                area += 1

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx = x + dx
                    ny = y + dy

                    if n > nx >= 0 and m > ny >= 0 and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        stack.append((nx, ny))
            
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, get_area(i, j))

        return max_area
        
        