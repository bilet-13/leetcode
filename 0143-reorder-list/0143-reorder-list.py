# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        head_right_list = slow.next
        slow.next = None
        
        curr = head_right_list
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head_right_list = prev

        curr1 = head
        curr2 = head_right_list

        while curr1 and curr2:
            next_curr1 = curr1.next
            next_curr2 = curr2.next

            curr1.next = curr2
            curr2.next = next_curr1

            curr2 = next_curr2
            curr1 = next_curr1