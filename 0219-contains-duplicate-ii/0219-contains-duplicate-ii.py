class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        nums_in_window = defaultdict(int)

        for right in range(len(nums)):
            while left < right - k:
                nums_in_window[nums[left]] -= 1
                left += 1

            if nums_in_window[nums[right]] > 0:
                return True 

            nums_in_window[nums[right]] += 1
            
        return False
        