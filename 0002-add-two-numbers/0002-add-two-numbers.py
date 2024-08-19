# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = None
        carry = 0
        node = None
        while l1 or l2:
            num1 = l1.val if l1 != None else 0
            num2 = l2.val if l2 != None else 0
            sum_vals = (num1 + num2 + carry) % 10

            if head == None:
                head = ListNode(val=sum_vals)
                node = head
            else:
                node.next = ListNode(val=sum_vals)
                node = node.next
            carry = 1 if (num1 + num2 + carry) >= 10 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry == 1:
            node.next = ListNode(val=carry)
            node = node.next
        return head
            