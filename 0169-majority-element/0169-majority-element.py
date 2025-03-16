class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        element = nums[0]
        time = 1

        for num in nums:
            if num != element:
                time -= 1

            if time == 0:
                element = num
                time = 1

        return element

        