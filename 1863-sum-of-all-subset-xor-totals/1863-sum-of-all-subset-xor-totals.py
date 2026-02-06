class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
           # use
        result = []
        cur = 0

        def backtrack(cur, idx, result):
            result.append(cur)

            for i in range(idx, len(nums)):
                backtrack(cur ^ nums[i], i + 1, result) 
            
            return
        
        backtrack(0, 0, result)

        return sum(result)



        