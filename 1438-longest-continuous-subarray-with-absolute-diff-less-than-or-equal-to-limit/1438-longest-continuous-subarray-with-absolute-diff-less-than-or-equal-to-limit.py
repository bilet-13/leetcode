class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # num[i] is positvee 
        # so just to make sure the difference between max and min <= limit
        # use two queue to find max and min for the subarry

        min_queue = deque()
        max_queue = deque()
        result = 1
        left = 0

        for right in range(len(nums)):
            num = nums[right]

            while min_queue and nums[min_queue[-1]] >= num:
                min_queue.pop()
            min_queue.append(right)

            while max_queue and nums[max_queue[-1]] <= num:
                max_queue.pop()
            max_queue.append(right)

            while left <= right and nums[max_queue[0]] - nums[min_queue[0]] > limit:
                left += 1
                while max_queue and max_queue[0] < left:
                    max_queue.popleft()
                while min_queue and min_queue[0] < left:
                    min_queue.popleft()
            
            result = max(result, right - left + 1)

        return result

        