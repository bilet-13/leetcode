class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_end = m - 1
        nums2_end = n - 1

        for index in range(m + n - 1, -1, -1):
            if nums1_end >= 0 and nums2_end >= 0:
                if nums1[nums1_end] > nums2[nums2_end]:
                    nums1[index] = nums1[nums1_end]
                    nums1_end -= 1
                else:
                    nums1[index] = nums2[nums2_end]
                    nums2_end -= 1

            elif nums1_end >= 0:
                nums1[index] = nums1[nums1_end]
                nums1_end -= 1
            else:
                nums1[index] = nums2[nums2_end]
                nums2_end -= 1



