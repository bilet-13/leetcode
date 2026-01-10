class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
                  # find the proper sum of each subarray
        # binary search

        left = max(nums)
        right = sum(nums)

        def box_needed(capacity):
            box_needed = 1
            cur_load = 0

            for n in nums:
                cur_load += n

                if cur_load > capacity:
                    box_needed += 1
                    cur_load = n

            return box_needed <= k

        while left <= right:
            mid = (right + left) // 2

            if box_needed(mid):
                right = mid - 1

            else:
                left = mid + 1

        return left
        
        