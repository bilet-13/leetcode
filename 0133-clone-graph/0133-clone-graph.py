"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from copy import deepcopy
from typing import Optional
class Solution:
    def clone_BFS(self, root_node, clone_root_node):
	
        queue = [(root_node, clone_root_node)]
        clone_graph = {root_node.val: clone_root_node}

        while queue:
            node, clone_node = queue.pop(0) 

            for neighbor_node in node.neighbors:
                if neighbor_node.val not in clone_graph.keys():
                    clone_neighbor = Node(neighbor_node.val, [])
                    clone_graph[neighbor_node.val] = clone_neighbor

                    queue.append((neighbor_node, clone_neighbor))

                clone_node.neighbors.append(clone_graph[neighbor_node.val])


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return node

        clone_root_node = Node(node.val, [])
        self.clone_BFS(node, clone_root_node)
        return clone_root_node
        