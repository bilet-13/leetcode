# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        node = head

        while node:
            if node.next and node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next

        return head

        