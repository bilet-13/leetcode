# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right == left:
            return head

        slow = head
        dummy = ListNode(next=slow)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next
        
        cur = prev.next
        prev_node = None

        for _ in range(left, right + 1):
            next_ptr = cur.next
            cur.next = prev_node
            prev_node = cur
            cur = next_ptr
        
        prev.next.next = cur
        prev.next = prev_node

        return dummy.next



       

        
        
        