# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head

        # find n+1th node form the end of the list
        slow = dummy_node
        fast = dummy_node
        distance_between_slow_fast = 0

        while distance_between_slow_fast < n + 1 and fast:
            fast = fast.next
            distance_between_slow_fast += 1
        
        while fast:
            fast = fast.next
            slow = slow.next

        #remove nth node ( n+1th node next = n - 1 th node )
        nth_node = slow.next
        slow.next = nth_node.next

        
        # return head
        return dummy_node.next


        