class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set()
        set2 = set()

        for num in nums1:
            set1.add(num)
        
        for num in nums2:
            set2.add(num)

        unique_set1 = (set1 ^ set2) & set1
        unique_set2 = (set1 ^ set2) & set2

        return [list(unique_set1), list(unique_set2)]

