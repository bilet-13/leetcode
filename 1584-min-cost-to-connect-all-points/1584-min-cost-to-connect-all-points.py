class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = []
        min_cost = 0
        n = len(points)
        parent = [i for i in range(n)]
        in_mst_edge_num = 0

        for i in range(n):
            fr_x, fr_y = points[i]
            for j in range(i + 1, n):
                to_x, to_y = points[j]
                heapq.heappush(pq, (abs(fr_x - to_x) + abs(fr_y - to_y), i, j))

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return parent[x]

        def union(x, y):
            parent[find(x)] = parent[find(y)]

        while in_mst_edge_num < n - 1:
            cost, fr, to = heapq.heappop(pq)

            if find(fr) == find(to):
                continue

            in_mst_edge_num += 1
            min_cost += cost
            union(fr, to)
        
        return min_cost
        