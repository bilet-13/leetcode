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
        if not head.next or not head.next.next:
            return False
        hare = head.next.next
        turtle = head.next

        while hare:
            if hare is turtle:
                return True
            if not hare.next or not hare.next.next or not turtle.next:
                break
            hare = hare.next.next
            turtle = turtle.next

        return False

        