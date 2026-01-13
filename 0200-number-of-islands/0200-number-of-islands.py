class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # for each land , do bfs to find its correspond island and mark the visited cell to prevent 
        # bfs again
        # time complexity o(mn)

        island_num = 0
        m = len(grid)
        n = len(grid[0])

        def bfs(start_x, start_y):
            queue = deque([(start_x, start_y)])
            grid[start_x][start_y] == '2' # prevent revisiting

            while queue:
                x, y = queue.popleft()

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx = x + dx
                    ny = y + dy

                    if m > nx >= 0 and n > ny >= 0 and grid[nx][ny] == '1':
                        grid[nx][ny] = '2'
                        queue.append((nx, ny)) 

        for i in range(len(grid)): # is the list may be empty?
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i, j)
                    island_num += 1
        
        return island_num