class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(cur, start, result):
            if sum(cur) > target:
                return

            elif sum(cur) == target:
                result.append(cur[:])
                return

            for i in range(start, len(candidates)):
                cur.append(candidates[i])
                backtrack(cur, i, result)
                cur.pop()


        result = []
        backtrack([], 0, result)
        return result
            
        
        