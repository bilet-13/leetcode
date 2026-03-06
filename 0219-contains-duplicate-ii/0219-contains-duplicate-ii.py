class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
         # sliding window keep the window size <= k
        left = 0
        nums_in_window = defaultdict(int)

        for right in range(len(nums)):
            nums_in_window[nums[right]] += 1

            while right - left > k:
                nums_in_window[nums[left]] -= 1
                left += 1

            if nums_in_window[nums[right]] == 2:
                return True  
        
        return False

        

        