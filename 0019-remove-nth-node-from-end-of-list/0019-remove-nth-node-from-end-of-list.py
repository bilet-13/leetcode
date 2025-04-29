# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        # find n+1th node form the end of the list
        # use slow, fast pointer
        slow = dummy
        fast = dummy
        
        for _ in range(n + 1):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next

        #remove nth node ( n+1th node next = n - 1 th node )
        slow.next = slow.next.next

        # return head
        return dummy.next