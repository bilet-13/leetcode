class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = [0] * (m+n)
        index1 = 0
        index2 = 0
        index3 = 0

        while index1 < m and index2 < n:
            if(nums1[index1] <= nums2[index2]):
                nums3[index3] = nums1[index1]
                index1 += 1
            else:
                nums3[index3] = nums2[index2]
                index2 += 1
            index3 += 1

        if index1 != m:
            while index1 < m: 
                nums3[index3] = nums1[index1]
                index1 += 1
                index3 += 1

        elif index2 != n:
            while index2 < n: 
                nums3[index3] = nums2[index2]
                index2 += 1
                index3 += 1
        
        for i in range(len(nums3)):
            nums1[i] = nums3[i]