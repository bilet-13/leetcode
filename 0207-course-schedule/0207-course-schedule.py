class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
           # topological sort or no cycle
        # check the graph has cycle or not
        # node: label of couse . edge b -> a if b is prerequisite course of a
        # use list[numCourse] to check visite or not 
        # for not state cell, do dfs to check is there has cycle
        # time complexity o(V + E) = o(n ^ 2)
        # edge case if numCOurse = 1 return true if len of prerequisites == 0 return true
        if numCourses <= 1 or len(prerequisites) < 1:
            return True
        state = [0 for _ in range(numCourses)] # 0 unstate 1 visiting 2 vistied
        edges = [[] for _ in range(numCourses)]
        for request in prerequisites:
            edges[request[1]].append(request[0])

        def check_cycle(node):
            stack = [(node, 0)]

            while stack:
                node, phase = stack.pop()

                if phase == 0:
                    if state[node] == 2:
                        continue
                    elif state[node] == 1:
                        return True
                    
                    state[node] = 1
                    stack.append((node, 1))
                    for course in edges[node]:
                        if state[course] == 1:
                            return True
                        elif state[course] == 0:
                            stack.append((course, 0))
                else:
                    state[node] = 2
    
            return False

        for i in range(numCourses):
            if state[i] == 0:
                if check_cycle(i):
                    return False
        return True

        