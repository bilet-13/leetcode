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
        clone_map = {node.val: Node(val=node.val)} #  key: node label val: copied node object

        while queue:
            cur = queue.popleft()

            for adj in cur.neighbors:
                if adj.val not in clone_map:
                    copied_node = Node(val=adj.val)
                    clone_map[adj.val] = copied_node
                    queue.append(adj)

                clone_map[cur.val].neighbors.append(clone_map[adj.val])

        return clone_map[node.val]




        
        
        