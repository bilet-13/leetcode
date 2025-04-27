# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1 8 2 3 4 5 6 7    
        # 1 2 3 4 5 6 7      
        # 1 8 2 7 3 6 4 5
        # 1 8 2 7 3 6 4 5
        curr = head
        
        while curr.next and curr.next.next:
            second_last = curr
            while second_last.next.next:
                second_last = second_last.next
            
            tail_node = second_last.next
            second_last.next = None
            
            next_curr = curr.next
            curr.next = tail_node
            tail_node.next = next_curr
            curr = next_curr


        




        