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
        if not root:
            return root
        next_row_head = None
        next_prev = None
        cur = root

        while cur:
            while cur:
                if cur.left:
                    if next_prev:
                        next_prev.next = cur.left
                    else:
                        next_row_head = cur.left
                    next_prev = cur.left

                if cur.right:
                    if next_prev:
                        next_prev.next = cur.right
                    else:
                        next_row_head = cur.right
                    next_prev = cur.right
                cur = cur.next

            cur = next_row_head
            next_row_head = None
            next_prev = None
                        

        return root

