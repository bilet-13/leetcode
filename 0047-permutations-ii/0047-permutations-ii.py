class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # how to prvent duplicate permutaion -> to prevent selecting the same number in the same level
        # how skip the duplicate num in currrent level

        nums.sort()

        def backtrack(start, result):
            if start == len(nums):
                result.append(nums[:])
                return

            used = set()

            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                
                used.add(nums[i])
                nums[i], nums[start] = nums[start], nums[i]

                backtrack(start + 1, result)

                nums[i], nums[start] = nums[start], nums[i]


        result = []
        backtrack(0, result)

        return result
        