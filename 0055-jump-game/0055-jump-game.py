class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start_index = 0

        while start_index < len(nums):
            next_max_jump = (nums[start_index], start_index)

            for i in range(1, nums[start_index]+1):
                fartest_position = next_max_jump[0] + next_max_jump[1]
                element_index = start_index + i

                if element_index < len(nums) and nums[element_index] + element_index > fartest_position:
                    next_max_jump = (nums[element_index], element_index)
            
            if start_index == next_max_jump[1]:
                return start_index + nums[start_index] >= len(nums) - 1

            start_index = next_max_jump[1]

        return True




        

        