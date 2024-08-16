class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp_canJump = [False for _ in range(len(nums))]
        dp_canJump[-1] = True

        for i in range(len(nums)-2, -1, -1):
            for j in range(0, nums[i]+1):
                if i + j > len(nums) - 1:
                    break
                dp_canJump[i] |= dp_canJump[i+j]
                if dp_canJump[i]:
                    break

        return dp_canJump[0]

    def _canJump(self, nums, cur):
        if cur >= len(nums) - 1:
            return true
        result = False

        for next_cur in range(1, nums[cur]+1):
            result |= self._canJump(nums, next_cur) 
        return result

