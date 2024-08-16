class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        invert_nums = [-num for num in nums]
        heapq.heapify(invert_nums)
        for i in range(k-1):
            heapq.heappop(invert_nums)
        result = -heapq.heappop(invert_nums)
        return result