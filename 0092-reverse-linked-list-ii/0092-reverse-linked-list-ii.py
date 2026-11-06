# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(next=head)
        end = dummy
        start = dummy

        for _ in range(left - 1):
            start = start.next
        
        before = start
        start = start.next

        for _ in range(right):
            end = end.next

        after = end.next
        node = start
        
        prev = None
        while node != after:
            node_nxt = node.next
            node.next = prev
            prev = node
            node = node_nxt
        
        before.next = prev
        start.next = after

        return dummy.next


        

        