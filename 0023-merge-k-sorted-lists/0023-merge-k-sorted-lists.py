# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # use min heap to store k node from k lists
        # each time pop one and append to result if the one has next push into heap
        # use dummy head to handle head and empty list
        # return dummy.next

        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i ,lists[i].next))
        
        dummy = ListNode()
        node = dummy
        while min_heap:
            smallest, idx, nxt = heapq.heappop(min_heap)
            node.next = ListNode(val=smallest)
            node = node.next

            if nxt:
                heapq.heappush(min_heap, (nxt.val, idx , nxt.next))

        return dummy.next



        