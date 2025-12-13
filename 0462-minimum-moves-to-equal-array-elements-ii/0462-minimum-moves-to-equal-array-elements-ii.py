class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # every num need to == avg(nums)
        nums.sort()
        medium = nums[len(nums) // 2]

        # 4 + 5 + 3 + 4
        min_moves = 0

        for num in nums:
            min_moves += abs(medium - num)

        return min_moves

        