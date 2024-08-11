# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        val_map = {}

        if not head:
            return False
        node = head

        while node:
            if node not in val_map:
                val_map[node] = True
            else:
                return True
            node = node.next
        
        return False

        