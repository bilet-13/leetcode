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
        cur = dummy

        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
                
            elif l1:
                cur.next = l1
                break
            else:
                cur.next = l2
                break
            
        return dummy.next



        