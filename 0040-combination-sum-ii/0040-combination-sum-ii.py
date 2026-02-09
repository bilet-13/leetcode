class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
           # right solution use set to record the same element we have used to prevent the duplicate combination
        # time complexity o(nlogn + n ^ (target / minium element))
        candidates.sort()

        def backtrack(cur, start, result, target):
            sum_cur = sum(cur)
            if target == 0:
                result.append(cur[:])
                return

            elif target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                cur.append(candidates[i])

                backtrack(cur, i + 1, result, target - candidates[i])

                cur.pop()
        
        result = []
        backtrack([], 0, result, target)

        return result
            
        