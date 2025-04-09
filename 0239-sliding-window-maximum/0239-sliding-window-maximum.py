class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        max_queue = deque()
        max_window = []

        for end in range(len(nums)):
            while max_queue and max_queue[-1][1] < nums[end]:
                max_queue.pop()
            max_queue.append([end, nums[end]])

            while max_queue and max_queue[0][0] < start:
                max_queue.popleft()
            
            if end - start + 1 == k:
                max_window.append(max_queue[0][1])
                start += 1
             
        return max_window