class Solution:
     def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        # heapq use min_heap to simulate max heap
        max_heap = []
        for weight in stones:
            heapq.heappush(max_heap, -weight)

        while len(max_heap) > 1:
            top1 = heapq.heappop(max_heap)
            top2 = heapq.heappop(max_heap)

            weight1 = -top1
            weight2 = -top2

            if weight1 == weight2:
                continue
            else:
                heapq.heappush(max_heap, -(weight1 - weight2))
        
        return -max_heap[0] if max_heap else 0
        
        