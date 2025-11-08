class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
         in_degrees = [0 for _ in range(numCourses)]
        edges = [[] for _ in range(numCourses)]
        order = []

        for prereq in prerequisites:
            edges[prereq[1]].append(prereq[0])
            in_degrees[prereq[0]] += 1
        
        starts = [course for course in range(numCourses) if in_degrees[course] == 0]

        while starts:
            cur = starts.pop()
            order.append(cur)

            for nxt in edges[cur]:
                in_degrees[nxt] -= 1
                if in_degrees[nxt] == 0:
                    starts.append(nxt)  
        
        return order if len(order) == numCourses else []
        