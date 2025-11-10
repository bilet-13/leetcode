class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        in_degrees = [0 for _ in range(numCourses)]

        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
            in_degrees[pre[1]] += 1

        order = {}
        queue = deque((i, 0) for i in range(numCourses) if in_degrees[i] == 0) 

        def check_connected(x, y):
            visited = [False for _ in range(numCourses)]
            stack = [x]
            visited[x] = True

            while stack:
                cur = stack.pop()

                if cur == y:
                    return True

                for nxt in graph[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        stack.append(nxt)

            return False
                
        # queue to start topological que((node, level))
        # use hash map to store the level
        while queue:
            cur, cur_order = queue.popleft()

            order[cur] = cur_order

            for nxt in graph[cur]:
                in_degrees[nxt] -= 1

                if in_degrees[nxt] == 0:
                    queue.append((nxt, cur_order + 1))

        # for each query check level
        return [check_connected(u, v) and order[u] < order[v] for u, v in queries]


 