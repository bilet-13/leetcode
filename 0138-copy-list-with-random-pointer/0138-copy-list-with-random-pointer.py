"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        while curr:
            next_node = curr.next
            curr.next = Node(curr.val, next=next_node)
            curr = next_node

        curr = head

        while curr:
            curr.next.random = curr.random.next if curr.random is not None else None
            curr = curr.next.next
        
        new_head = head.next if head is not None else None
        curr = new_head

        while curr and curr.next:
            curr.next = curr.next.next
            curr = curr.next

        return new_head

        
        