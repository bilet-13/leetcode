class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # double pointer o(n)
        # first pointer : index of result
        # second pointer : index of origin nums
        non_val_idx = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[non_val_idx] = nums[i]
                non_val_idx += 1

        return non_val_idx

