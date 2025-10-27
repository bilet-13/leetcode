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
        """
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        # create new node as copied root
        # use hash map to store the copied node , key: node label val: copied node object
        # Use BFS to iterate the graph start with input node
        # use arr[n] as visited set
        # for each visited node in bfs create it and store its val add neighbor to it
        # add the unviisted neightbor into queue

        queue = deque([node])
        copied_nodes = {}
        visited = set([node.val])

        while queue:
            cur = queue.popleft()

            if cur.val not in copied_nodes:
                copied_node = Node(val=cur.val)
                copied_nodes[cur.val] = copied_node

            for neighbor in cur.neighbors:
                if neighbor.val not in copied_nodes:
                    copied_node = Node(val=neighbor.val)
                    copied_nodes[neighbor.val] = copied_node

                copied_nodes[cur.val].neighbors.append(copied_nodes[neighbor.val])

                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    queue.append(neighbor)

        return copied_nodes[node.val]




        
        
        