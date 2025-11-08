class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0 for _ in range(numCourses)]
        edges = [[] for _ in range(numCourses)]
        has_cycle = False
        order = []

        for pre in prerequisites:
            edges[pre[1]].append(pre[0])

        def DFS(cur):
            nonlocal has_cycle
            if visited[cur] == 2:
                return
            elif visited[cur] == 1:
                has_cycle = True
                return

            visited[cur] = 1
            for nxt in edges[cur]:
                DFS(nxt)

            visited[cur] = 2
            order.append(cur)
            return

        for course in range(numCourses):
            if visited[course] == 0:
                DFS(course)
        
        return [] if has_cycle else order[::-1]
        