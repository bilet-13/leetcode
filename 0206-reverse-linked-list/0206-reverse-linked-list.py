# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        def reverse(node):
            if node is None or node.next is None:
                return node
            
            last = reverse(node.next)
            nxt_node = node.next
            nxt_node.next = node # brillent step
            node.next = None

            return last

        return reverse(head)
        