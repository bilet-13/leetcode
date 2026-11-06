# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(next=head)
        fast = dummy
        slow = dummy

        for _ in range(left - 1):
            slow = slow.next
        
        prev = slow
        slow = slow.next

        for _ in range(right):
            fast = fast.next

        nxt = fast.next
        node = slow
        
        node_prev = None
        while node and node != nxt:
            node_nxt = node.next
            node.next = node_prev
            node_prev = node
            node = node_nxt
        
        prev.next = node_prev
        slow.next = nxt

        return dummy.next


        

        