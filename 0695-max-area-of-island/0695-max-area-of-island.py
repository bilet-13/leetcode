class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
         # and update the max area variable
        maxArea = 0 
        n = len(grid)
        m = len(grid[0])

        def BFS(r, c):
            area = 0
            queue = deque([(r, c)])
            grid[r][c] = 2

            while queue:
                x, y = queue.popleft()

                area += 1

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx = x + dx
                    ny = y + dy

                    if n > nx >= 0 and m > ny >= 0 and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
            return area

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, BFS(i, j))

        return maxArea
        
        