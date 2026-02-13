class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
         # search in the tree
        # prevent the same number in the same level on the tree
        nums.sort()

        def backtrack(cur, start, result):
            result.append(cur[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                cur.append(nums[i])
                
                backtrack(cur, i + 1, result)

                cur.pop()

        result = []
        backtrack([], 0, result)

        return result


        
        