class Solution:
    def find_topological_order(self, graph):
	# 1 initial a list called oreders, a queue called tmp_queue find all nodes whose in_degreee == 0 if found add the nodes into tmp_queue  and orederselse return []
	#2 while tmp_queue is not empty, pop one node for all neighbor the node pointing, remove the edge between them , if the neighbor  in_degreee == 0 add the nodes into tmp_queue  and 	oreders
# 3 we check the node number of the oredersif len(oreders) == len(graph) return oreders else return []
        orders = [node for node in graph if not graph[node]['in'] ]
        tmp_queue = deque(orders )

        while tmp_queue:
            node = tmp_queue.pop()
            for neighbor in graph[node]['out']:
                graph[neighbor]['in'].remove(node)

                if not graph[neighbor]['in']:
                    tmp_queue.append(neighbor)
                    orders.append(neighbor) 

        if len(orders) == len(graph):
            return orders
        return []

    def build_graph(self, numCourses , prerequisites):
        #build nodes
        graph = {i: {'in': [], 'out': []} for i in range(numCourses)}
        
        #build edges
        for ai, bi in prerequisites:
            graph[bi]['out'].append(ai)
            graph[ai]['in'].append(bi)

        return graph

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph =  self.build_graph(numCourses , prerequisites)
        return self.find_topological_order(graph)
