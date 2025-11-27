class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        dist = [float("inf") for _ in range(n)]
        dist[src] = 0

        for fr, to, price in flights:
            graph[fr].append((to, price))

        for t in range(k + 1):
            cur_dist = deepcopy(dist)
            for start in range(n):
                for nbr, price in graph[start]:
                    cost = cur_dist[start] + price 
                    if cost < dist[nbr]:
                        dist[nbr] = cost
        
        return dist[dst] if dist[dst] != float("inf") else -1

        