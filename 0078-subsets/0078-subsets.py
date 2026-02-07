class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(cur, idx, result):
            result.append(cur[:])

            for i in range(idx, len(nums)):
                cur.append(nums[i])
                backtrack(cur, i + 1, result)
                cur.pop()
            
            return
        
        result = []
        backtrack([], 0, result)

        return result
        