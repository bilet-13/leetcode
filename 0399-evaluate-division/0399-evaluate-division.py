class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        values_graph = {}
        for i in range(len(equations)):
            if equations[i][0] not in values_graph:
                values_graph[equations[i][0]] = []
            values_graph[equations[i][0]].append((equations[i][1], values[i]))
            
            if equations[i][1] not in values_graph:
                    values_graph[equations[i][1]] = []

            values_graph[equations[i][1]].append((equations[i][0], float(1 / values[i]) ) )

        results = []

        for i in range(len(queries)):
            if queries[i][0] not in values_graph or queries[i][1] not in values_graph:
                results.append(-1.0)
                
            elif queries[i][0] == queries[i][1]:
                results.append(1.0)
            else:
                results.append(self.DFS(queries[i][0], queries[i][1], values_graph))

                
        return results

    def DFS(self, start, end, graph):

        stack = [(start, 1)]
        visited = {start: 1}


        while stack:
            node, value = stack.pop(-1)
            
            for neighbor, weight in graph[node]:
                if neighbor == end:
                    return value*weight
                if neighbor not in visited:
                    visited[neighbor] = 1
                    stack.append((neighbor, value*weight))
                
        return -1.0
