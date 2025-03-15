class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = self.getUniqueNums(nums1)
        set2 = self.getUniqueNums(nums2)

        unique_set1 = (set1 ^ set2) & set1
        unique_set2 = (set1 ^ set2) & set2

        return [list(unique_set1), list(unique_set2)]

    def getUniqueNums(self, nums):
        unique_nums = set()
        for num in nums:
            unique_nums.add(num)

        return unique_nums



