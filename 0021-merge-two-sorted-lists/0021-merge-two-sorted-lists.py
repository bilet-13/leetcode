# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        l1 = list1
        l2 = list2
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1 and l2:
                if l1.val < l2.val:
                    node = l1
                    l1 = l1.next
                else:
                    node = l2
                    l2 = l2.next
                tail.next = node
                tail = tail.next

        tail.next = l1 if l1 else l2
            
        return dummy.next



        