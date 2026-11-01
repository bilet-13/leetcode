class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = [] # store the k largest elements so the top elemnt is the kth largest elemet
        for num in nums:
            if len(self.min_heap) < self.k:
                heapq.heappush(self.min_heap, num)
            else:
                if self.min_heap[0] < num:
                    heapq.heappop(self.min_heap)
                    heapq.heappush(self.min_heap, num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            if self.min_heap[0] < val:
                heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, val)
            
        return self.min_heap[0]


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)