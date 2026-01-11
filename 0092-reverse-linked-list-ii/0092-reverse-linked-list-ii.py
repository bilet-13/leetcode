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

        for _ in range(0, left - 1):
            prev = prev.next
            slow = slow.next
        reverse_tail = slow

        fast = head
        for _ in range(0, right - 1):
            fast = fast.next
        tail = fast.next
        reverse_head = fast 

        start = left

        follower = None
        while start <= right:
            next_ptr = slow.next
            slow.next = follower 
            follower = slow
            slow = next_ptr

            start += 1
        
        prev.next = reverse_head
        reverse_tail.next = tail

        return dummy.next

        
        
        