class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []

        for i in range(len(nums)):
            num = nums[i]
            
            while queue and queue[0] <= (i - k):
                queue.popleft()

            while queue and nums[queue[-1]] <= num:
                queue.pop()

            queue.append(i)
            
            if i >= k - 1:
                result.append(nums[queue[0]])
        
        return result