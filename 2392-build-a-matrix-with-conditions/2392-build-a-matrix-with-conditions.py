class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_graph = {i: [] for i in range(1, k + 1)}
        row_indegrees = {i: 0 for i in range(1, k + 1)}

        for above, below in rowConditions:
            row_graph[above].append(below)
            row_indegrees[below] += 1

        col_graph = {i: [] for i in range(1, k + 1)}
        col_indegrees = {i: 0 for i in range(1, k + 1)}

        for left, right in colConditions:
            col_graph[left].append(right)
            col_indegrees[right] += 1

        def find_topological_order(graph, indegrees):
            starts = [node for node in indegrees if indegrees[node] == 0]
            queue = deque(starts)
            order = []

            while queue:
                cur = queue.popleft()

                order.append(cur)

                for nbr in graph[cur]:
                    indegrees[nbr] -= 1

                    if indegrees[nbr] == 0:
                        queue.append(nbr)
            
            return order if len(order) == k else []

        row_order = find_topological_order(row_graph, row_indegrees)
        col_order = find_topological_order(col_graph, col_indegrees)

        if len(row_order) == 0 or len(col_order) == 0:
            return []
        
        result_matrix = [[0 for _ in range(k)] for _ in range(k)]
        row_indices = {num: idx for idx, num in enumerate(row_order)}
        col_indices = {num: idx for idx, num in enumerate(col_order)}

        for num, r_idx in row_indices.items():
            c_idx = col_indices[num]
            result_matrix[r_idx][c_idx] = num
        
        return result_matrix

        