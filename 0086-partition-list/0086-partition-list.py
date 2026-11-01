# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy_less = ListNode()
        dummy_larger = ListNode()
        less = dummy_less
        larger = dummy_larger

        node = head
        while node:
            nxt = node.next
            node.next = None
            if node.val < x:
                less.next = node
                less = less.next
            else:
                larger.next = node
                larger = larger.next
            node = nxt
        
        if dummy_less.next:
            less.next = dummy_larger.next
            return dummy_less.next
        else:
            return dummy_larger.next
        

        