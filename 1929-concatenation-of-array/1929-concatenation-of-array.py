class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        concatenaion_arr = [0 for _ in range(2 * n)]

        for i in range(n):
            concatenaion_arr[i] = nums[i]
            concatenaion_arr[i + n] = nums[i]
        return concatenaion_arr
        