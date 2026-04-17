class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        min_cost = {(i, j): float("inf")  for i in range(len(heights)) for j in range(len(heights[0]))}
        min_heap = [(0, 0, 0)]
        min_cost[(0, 0)] = 0
        n = len(heights)
        m = len(heights[0])

        while min_heap:
            effort, x, y = heapq.heappop(min_heap)
            
            if x ==  n - 1 and y == m - 1:
                return effort
            
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nx = x + dx
                ny = y + dy

                if n > nx >= 0 and m > ny >= 0 and max(effort, abs(heights[x][y] - heights[nx][ny])) < min_cost[(nx, ny)]:
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    heapq.heappush(min_heap, (new_effort, nx, ny))
                    min_cost[(nx, ny)] = new_effort
        return min_cost[(n - 1, m - 1)]
        