class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        # brute force: use backtracking to find permuatitons
        #  return the minimual XOR Sum of nums1 and one of the permuaitons of nums2
        # beacuse the probiem fit the makov property -> so can use dp/memo
        minimum_xor_sum = float("inf")
        n = len(nums1)

        @cache
        def dp(mask):
            cur_idx = mask.bit_count()
            if cur_idx == n:
                return 0

            min_subproblem_sum = float("inf")

            for i in range(n):
                if mask & (1 << i) == 0:
                    xor_sum = nums1[cur_idx] ^ nums2[i]

                    sub_result = dp(mask | (1 << i))

                    min_subproblem_sum = min(min_subproblem_sum, xor_sum + sub_result)

            return min_subproblem_sum

        return dp(0)





        