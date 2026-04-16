# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow, fast pointer
        # slow took one step and fast took two steps each time untile fast reach the end or it can not jump twice and check if there is still a node if yes return 
        # 1 2 3 4 5 
        # start from 1 fast 1 3 5, slow 1 2 3 return slow
        # 1 2 3 4 5 6        
        # start from 1 fast 1 3 5, slow 1 2 3  return slow.next

        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow.next if fast.next else slow