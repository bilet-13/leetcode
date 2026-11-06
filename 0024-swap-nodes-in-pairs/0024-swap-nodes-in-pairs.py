# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:

        # one pass?
        # node -> the first node
        # node.next -> second node
        dummy = ListNode(next=head)
        prev = dummy

        node = head
        while node and node.next:
            first = node
            second = node.next

            first.next = second.next
            second.next = first

            prev.next = second
            prev = first

            node = node.next

        return dummy.next
        