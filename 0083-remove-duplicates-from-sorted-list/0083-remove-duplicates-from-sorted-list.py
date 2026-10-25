# Definition for singly-linked list.
# class Listlast_unique:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Listlast_unique | None) -> Listlast_unique | None:
        last_unique = head

        while last_unique:
            while last_unique.next and last_unique.next.val == last_unique.val:
                last_unique.next = last_unique.next.next
            last_unique = last_unique.next

        return head

        