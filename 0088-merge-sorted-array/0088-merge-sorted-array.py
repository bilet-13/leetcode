class Solution: 
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return

        merge_idx = m + n - 1
        nums1_idx = m - 1
        nums2_idx = n - 1

        while merge_idx >= 0:
            if (nums1_idx >= 0 and nums1[nums1_idx] >= nums2[nums2_idx] and nums2_idx >= 0) or  nums2_idx < 0:
                nums1[merge_idx] = nums1[nums1_idx]
                nums1_idx -= 1
            else:
                nums1[merge_idx] = nums2[nums2_idx]
                nums2_idx -= 1
            
            merge_idx -= 1

        return 