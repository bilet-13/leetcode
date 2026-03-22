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

        labels_to_new_nodes = {node.val: Node(val=node.val)}
        stack = [node]

        while stack:
            n = stack.pop()

            for nbr in n.neighbors:
                if nbr.val not in labels_to_new_nodes:
                    labels_to_new_nodes[nbr.val] = Node(val=nbr.val)
                    stack.append(nbr)
                
                labels_to_new_nodes[n.val].neighbors.append(labels_to_new_nodes[nbr.val])

        return labels_to_new_nodes[1]

        
        