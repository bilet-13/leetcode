class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # travsal every unvisited cell do BFS and 
        # mark the vistied cell to 2
        # use var to count the num of island
        count = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0])

        def BFS(grid, i, j):
            queue = deque()
            queue.append((i, j))
            grid[i][j] = '2'

            while queue:
                x, y = queue.popleft()

                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy

                    if m > nx >= 0 and n > ny >= 0 and grid[nx][ny] == '1':
                        grid[nx][ny] = '2'
                        queue.append((nx, ny)) 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    BFS(grid, i, j)

        return count
        