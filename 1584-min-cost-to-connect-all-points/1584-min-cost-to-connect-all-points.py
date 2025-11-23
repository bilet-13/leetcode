class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = []
        n = len(points)
        min_cost = 0

        def add_edges(x, y):
            for nbr_x, nbr_y in points:
                if x == nbr_x and y == nbr_y:
                    continue
                heapq.heappush(pq, (abs(x - nbr_x) + abs(y - nbr_y), x, y, nbr_x, nbr_y))

        start_x, start_y = points[0][0], points[0][1] 
        in_mst = {(start_x, start_y)}
        add_edges(start_x, start_y)
        
        while len(in_mst) < n:
            cost, fr_x, fr_y, to_x, to_y = heapq.heappop(pq)
            if (to_x, to_y) in in_mst:
                continue
            
            min_cost += cost
            in_mst.add((to_x, to_y))

            add_edges(to_x, to_y)

        return min_cost
        