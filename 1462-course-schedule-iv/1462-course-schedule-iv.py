class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        connected = [[False for _ in range(numCourses)] for _ in range(numCourses)]

        for pre in prerequisites:
            connected[pre[0]][pre[1]] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    connected[i][j] |= connected[i][k] and connected[k][j]


        return [connected[u][v] for u, v in queries]


 