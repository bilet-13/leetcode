class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtraking
        # cur: the list to record numbers we choosed
        # start: define the start idx

        # base case: when length of cur == length of nums add the cur to result and return

        # else: start from idx and swap the number we choose


        def backtrack(cur, start, result):
            if start == len(nums):
                result.append(cur[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]# swap to make permutation
                cur.append(nums[start])

                backtrack(cur, start + 1, result)

                cur.pop()
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack([], 0, result)
        
        return result
        
    
