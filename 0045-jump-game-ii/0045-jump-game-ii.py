class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        pos = 0
        num_jump = 0
        farthest = 0 + nums[0]
        next_pos = 0
        
        while pos < len(nums):
            for i in range(1, nums[pos]+1):
                neighbor = pos + i
                if neighbor >= len(nums) - 1:
                     return num_jump + 1
                elif nums[neighbor] + neighbor > farthest:
                    farthest = nums[neighbor] + neighbor
                    next_pos = neighbor
                    
            num_jump += 1
            pos = next_pos
        
        return num_jump
