class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        if k == 0:
            return
        
        queue = deque()

        for i in range(k, 0, -1):
            queue.append(nums[len(nums)-i])

        for i in range(0, len(nums)-k):
            queue.append(nums[i])

        for i in range(len(nums)):
            nums[i] = queue.popleft()
            
