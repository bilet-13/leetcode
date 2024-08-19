class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_prefix = [None for _ in range(len(nums))]
        product_suffix = [None for _ in range(len(nums))]

        product_prefix[0] = 1
        product_suffix[-1] = 1

        for i in range(1, len(nums)):
            product_prefix[i] = product_prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            product_suffix[i] = product_suffix[i+1] * nums[i+1]

        answer = []
        for i in range(len(nums)):
            prefix = product_prefix[i]
            suffix = product_suffix[i]
            answer.append(prefix*suffix)
        return answer
         