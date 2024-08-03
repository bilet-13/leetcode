class Solution:
    def build_course_graph(self, numCourses, prerequisites):
        graph = {}

        for num in range(numCourses):
            graph[num] = {'out':[], 'in':[]}
        
        for course, pre_course in prerequisites:
            graph[pre_course]['out'].append(course)
            graph[course]['in'].append(pre_course)
        return graph

    def check_cycle(self, graph):

        queue = []
        visited = []
        for node in graph.keys():
            if not graph[node]['in']:
                queue.append(node)
                visited.append(node)

        if not queue:
            return True

        while queue:
            node = queue.pop(0)
            for ele in graph.keys():
                if node in graph[ele]['in']:
                    graph[ele]['in'].remove(node)

            for node in graph.keys():
                if not graph[node]['in'] and node not in visited:
                    queue.append(node)
                    visited.append(node)

            if not queue and len(visited) != len(graph.keys()):
                return True
                 
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = self.build_course_graph(numCourses, prerequisites)
        return not self.check_cycle(graph)
