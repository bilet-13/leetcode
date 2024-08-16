# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        head = None 
        cur = None
        while list1 and list2:
            if list1.val < list2.val:
                if head == None:
                    head = list1
                    cur = head
                else:
                    cur.next = list1
                    cur = cur.next
                list1 = list1.next
            else :
                if head == None:
                    head = list2
                    cur = head
                else:
                    cur.next = list2
                    cur = cur.next
                list2 = list2.next
        while list1:
            cur.next = list1
            cur = cur.next
            list1 = list1.next
        while list2:
            cur.next = list2
            cur = cur.next
            list2 = list2.next
        
        return head


