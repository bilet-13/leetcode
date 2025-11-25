class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # shortest path problem
        # find min max time path from 0,0 to n - 1, m - 1
        # path update formula max(dist, grid[nbr][nbr])
        # no negetive edge time >= 0, dijkstra algo
        # time complexity o(v + E))
        n = len(grid)
        m = len(grid[0])

        dist = [[float("inf") for _ in range(m)] for _ in range(n)]
        dist[0][0] = grid[0][0]
        pq = [(dist[0][0], 0, 0)]

        while pq:
            cur_t, cur_x, cur_y = heapq.heappop(pq)
            if cur_t > dist[cur_x][cur_y]:
                continue

            if cur_x == n - 1 and cur_y == m - 1:
                return cur_t 
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = cur_x + dx
                ny = cur_y + dy

                if n > nx >= 0 and m > ny >= 0:
                    n_time = max(cur_t, grid[nx][ny])

                    if n_time < dist[nx][ny]:
                        dist[nx][ny] = n_time
                        heapq.heappush(pq, (n_time, nx, ny))
        
        return -1

        
        