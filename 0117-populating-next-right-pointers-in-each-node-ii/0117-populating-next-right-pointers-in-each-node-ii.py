"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        depth_nodes = {}
        self.preorder_search_and_add_queue(root, depth_nodes, 0)

        for depth in depth_nodes:
            left = 0
            right = 1
            while right > left and right < len(depth_nodes[depth]):
                depth_nodes[depth][left].next = depth_nodes[depth][right]
                left += 1
                right += 1
        return root

    def preorder_search_and_add_queue(self, root, depth_nodes, depth):
        if not root:
            return
        if depth not in depth_nodes:
            depth_nodes[depth] = []
        depth_nodes[depth].append(root)
        
        self.preorder_search_and_add_queue(root.left, depth_nodes, depth+1)
        self.preorder_search_and_add_queue(root.right, depth_nodes, depth+1)
