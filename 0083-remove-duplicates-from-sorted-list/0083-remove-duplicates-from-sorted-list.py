# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(val=-111)
        tail = dummy

        node = head

        while node:
            if node.val != tail.val:
                tail.next = ListNode(val=node.val)
                tail = tail.next
            node = node.next

        return dummy.next

        