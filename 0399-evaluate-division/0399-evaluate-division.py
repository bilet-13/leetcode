class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list) # list of tuple node and val

        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1.0 / values[i]))
        
        n = len(graph)

        def BFS(start, target):
            visited = set(start)
            queue = deque([(start, 1)])

            while queue:
                cur, product = queue.popleft()

                if cur == target:
                    return product
                
                for nbr, val in graph[cur]:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append((nbr, product * val))

            return -1.0 

        return [BFS(start, target) if start in graph and target in graph else -1.0 for start, target in queries]


        