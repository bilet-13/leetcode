# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      # time complexity o(mlogk) m: the number of all eleemnt in resutl

        dummy = ListNode()
        cur = dummy
        min_heap = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))

        while min_heap:
            val, idx, node = heapq.heappop(min_heap)

            cur.next = node
            cur = cur.next

            nxt_node = node.next
            if nxt_node:
                heapq.heappush(min_heap, (nxt_node.val, idx, nxt_node))
        
        return dummy.next

        