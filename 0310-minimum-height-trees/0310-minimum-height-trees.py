class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        degrees = [0 for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        
        queue = deque([node for node in range(n) if degrees[node] == 1]) # start from leaves
        remain_nodes = set(range(n))

        while len(remain_nodes) > 2:
            size = len(queue)
            
            for i in range(size):
                cur = queue.popleft()

                remain_nodes.discard(cur)

                for nbr in graph[cur]:
                    degrees[nbr] -= 1
                    if degrees[nbr] == 1:
                        queue.append(nbr)
        
        return [node for node in remain_nodes]