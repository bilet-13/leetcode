class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_and_count = [nums[0], 1] # number, count

        for i in range(1, len(nums)):
            if nums[i] != num_and_count[0]:
                num_and_count[1] -= 1
                
                if num_and_count[1] == 0:
                    num_and_count = [nums[i], 1]
            else:
                num_and_count[1] += 1

        return num_and_count[0]

        