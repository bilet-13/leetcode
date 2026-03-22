"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
          # use hash map key: node label value: new node
        # time complexity o(V + E)
        if not node:
            return None

        labels_to_nodes = {}
        stack = [node]
        visited = set([node.val])

        while stack:
            n = stack.pop()

            if n.val not in labels_to_nodes:
                labels_to_nodes[n.val] = Node(val=n.val)

            for nbr in n.neighbors:
                if nbr.val not in labels_to_nodes:
                    labels_to_nodes[nbr.val] = Node(val=nbr.val)
                labels_to_nodes[n.val].neighbors.append(labels_to_nodes[nbr.val])
                
                if nbr.val not in visited:
                    stack.append(nbr)
                    visited.add(nbr.val)

        return labels_to_nodes[1]

        
        