class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # time complesity o(n * (V + E)) = o(n * n) = o(n ^ 2)
        graph = [[] for _ in range(n)]
        for edge in edges:
            u = edge[0]
            v = edge[1]

            graph[u].append(v)
            graph[v].append(u)

        def longest_path(root):
            parent = [-1 for _ in range(n)]
            visited = [False for _ in range(n)]
            path_len = 0
            path_end = root

            queue = deque([(root, -1, 0)]) # node, parent, len
            visited[root] = True

            while queue:
                cur, par, cur_len = queue.popleft()
                parent[cur] = par

                if path_len < cur_len:
                    path_len = cur_len
                    path_end = cur
                
                for nbr in graph[cur]:
                    if not visited[nbr]:
                        visited[nbr] = True
                        queue.append((nbr, cur, cur_len + 1))

            path = []
            cur = path_end
            while cur != -1:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            print(path)

            return path

        longest_path_for_0 = longest_path(0)
        root_diameter = longest_path_for_0[-1]
        diameter_path = longest_path(root_diameter)
        
        size = len(diameter_path)
        right = size - 1
        mid = right // 2

        return diameter_path[mid: mid + 1] if size % 2 == 1 else diameter_path[mid: mid + 2]
