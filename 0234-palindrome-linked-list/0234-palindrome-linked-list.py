# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        if fast: # odd 
            slow = slow.next

        #reverse second part
        prev = None
        node = slow
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        
        right = prev
        left = head

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

        