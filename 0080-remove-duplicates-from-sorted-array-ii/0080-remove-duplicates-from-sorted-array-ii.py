class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        [123334]
        [123343]
        cur = 0 
        end = len(nums)

        element = nums[cur]
        count = 1
        cur += 1

        while cur < end:
            if element == nums[cur] and count < 2:
                count += 1
                cur += 1
            elif element == nums[cur] and count == 2:
                self.push_end(nums, cur, end)
                end -= 1
            elif element != nums[cur]:
                element = nums[cur]
                count = 1
                cur += 1
        
        return end

    def push_end(self, nums, index, end):
        tmp_num = nums[index]
        for i in range(index, end-1):
            nums[i] = nums[i+1]
        nums[end-1] = tmp_num
