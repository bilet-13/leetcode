class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        unique_set1 = (set1 ^ set2) & set1
        unique_set2 = (set1 ^ set2) & set2

        return [list(unique_set1), list(unique_set2)]




