class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
          # no negative edge, dijkstra
        n = len(heights)
        m = len(heights[0])
        dist = [[float("inf") for _ in range(m)] for _ in range(n)]
        dist[0][0] = 0

        pq = [(dist[0][0], 0, 0)]

        while pq:
            effort, cur_x, cur_y = heapq.heappop(pq)
            if effort > dist[cur_x][cur_y]:
                continue

            if cur_x == n - 1 and cur_y == m - 1:
                return effort

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = cur_x + dx
                ny = cur_y + dy
                if n > nx >= 0 and m > ny >= 0:
                    nbr_cost = max(effort, abs(heights[nx][ny] - heights[cur_x][cur_y]))
                    if dist[nx][ny] > nbr_cost:
                        dist[nx][ny] = nbr_cost
                        heapq.heappush(pq, (nbr_cost, nx, ny))
        return 0
        