# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i, list_i in enumerate(lists):
            if list_i:
                heapq.heappush(min_heap, (list_i.val, i, list_i))

        dummy = ListNode()
        cur = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)

            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next


        