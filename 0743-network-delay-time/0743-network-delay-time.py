class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # directed graph with edge value node 1 to n
        # k start node
        # return the max shotest path from k to all other node if all node is visgtisted
        # otherwise return -1
        # ti is non negative
        # dijkstra to find single source shotest path
        # time complexity o((V + E)*logv) = o((n + len(times))*logn)
        graph = [[] for _ in range(n + 1)]
        for u, v, t in times:
            graph[u].append((v, t))

        total_time = [float("inf") for _ in range(n + 1)]
        total_time[k] = 0
        min_delay_time = 0
        pq = [(total_time[k], k)]

        while pq:
            time, cur = heapq.heappop(pq)
            if total_time[cur] < time:
                continue 
            
            min_delay_time = max(min_delay_time, time) 

            for nbr, nbr_time in graph[cur]:
                if time + nbr_time < total_time[nbr]:
                    total_time[nbr] = time + nbr_time
                    heapq.heappush(pq, (total_time[nbr], nbr))

        return min_delay_time if all(time != float("inf") for time in total_time[1:]) else -1




        