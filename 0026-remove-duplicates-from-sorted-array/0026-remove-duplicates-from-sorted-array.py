class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        num_has_appeared = set()
        unique_num = []

        for i in range(len(nums)):
            if nums[i] in num_has_appeared:
                continue
            else:
                unique_num.append(nums[i])
                num_has_appeared.add(nums[i])
        
        for i in range(len(unique_num)):
            nums[i] = unique_num[i]

        return len(unique_num)