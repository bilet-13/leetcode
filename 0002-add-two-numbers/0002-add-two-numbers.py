# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #initialize carry and new head
        carry = 0
        dummy = ListNode()
        current = dummy

        #Iterate through both lists until all nodes and carry are processed  
        while l1 or l2 or carry != 0:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            carry = math.floor(total / 10)
            digit = total % 10

            new_node = ListNode(val=digit)
            current.next = new_node
            current = current.next

        #return the new head
        return dummy.next
