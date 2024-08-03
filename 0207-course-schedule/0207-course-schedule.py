class Solution:
    def build_course_graph(self, numCourses, prerequisites):
        graph = {i:{'in':[], 'out': []} for i in range(numCourses)}
        
        for course, pre_course in prerequisites:
            graph[course]['in'].append(pre_course)
            graph[pre_course]['out'].append(course)
            
        return graph

    def check_cycle(self, graph):

        queue = deque([node for node in graph if not graph[node]['in']])
        visited = set(queue)

        if not queue:
            return True

        while queue:
            node = queue.pop()
            for neighbor in graph[node]['out']:
                graph[neighbor]['in'].remove(node)
                if not graph[neighbor]['in']:
                    queue.append(neighbor)
                    visited.add(neighbor)

            if not queue and len(visited) != len(graph.keys()):
                return True
                 
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = self.build_course_graph(numCourses, prerequisites)
        return not self.check_cycle(graph)
