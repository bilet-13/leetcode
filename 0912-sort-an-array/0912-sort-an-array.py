class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        sorted_nums = []

        while nums:
            cur_smallest = heapq.heappop(nums)
            sorted_nums.append(cur_smallest)
        
        return sorted_nums
        
        