class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        [123334]
        [123343]
        duplicated_num = nums[0]
        count = 1
        insert_pos = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if count < 2:
                    nums[insert_pos] = nums[i]
                    count += 1
                    insert_pos += 1
                else:
                    count += 1

            else:
                count = 1
                duplicated_num = nums[i]
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        
        return insert_pos

    def push_end(self, nums, index, end):
        tmp_num = nums[index]
        for i in range(index, end-1):
            nums[i] = nums[i+1]
        nums[end-1] = tmp_num
