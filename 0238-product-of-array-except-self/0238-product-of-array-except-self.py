class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for _ in range(len(nums))]
        prefix = 1
        suffix = 1

        for i in range(1, len(nums)):
            answer[i] *= prefix * nums[i-1]
            prefix *= nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            answer[i] *= suffix * nums[i+1]
            suffix *= nums[i+1]

        return answer
         