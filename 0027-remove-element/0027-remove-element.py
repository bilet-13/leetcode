class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        not_equal_nums = []
        for num in nums:
            if num == val:
                continue
            else:
                not_equal_nums.append(num)

        k = len(not_equal_nums)

        
        nums[:k] = not_equal_nums[:k]

        return k 
