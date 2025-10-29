class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # time complexity o(nm), calcuate roten and vvisited and fresh num  + BFS = o(V+E) = o(nm)

        fresh_num = sum([1 for i in range(m) for j in range(n) if grid[i][j] == 1])

        minimum_time = 0
        visited = [[False for j in range(n)] for i in range(m)]

        rottens = [(i, j, 0) for i in range(m) for j in range(n) if grid[i][j] == 2]
        queue = deque(rottens)

        while queue:
            x, y, time = queue.popleft()

            minimum_time = max(minimum_time, time)
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy

                if m > nx >= 0 and n > ny >= 0 and grid[nx][ny] == 1 and not visited[nx][ny]:
                    fresh_num -= 1
                    visited[nx][ny] = True
                    queue.append((nx, ny, time + 1))
        
        return minimum_time if fresh_num == 0 else -1