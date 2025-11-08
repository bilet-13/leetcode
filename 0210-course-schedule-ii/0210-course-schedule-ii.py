class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = [0 for _ in range(numCourses)]
        edges = [[] for _ in range(numCourses)]
        order = []

        for pre in prerequisites:
            edges[pre[1]].append(pre[0])
            in_degrees[pre[0]] += 1
        
        queue = deque(course for course in range(numCourses) if in_degrees[course] == 0)

        while queue:
            cur = queue.popleft()
            order.append(cur)

            for nxt in edges[cur]:
                in_degrees[nxt] -= 1
                if in_degrees[nxt] == 0:
                    queue.append(nxt)  
        
        return order if len(order) == numCourses else []
        