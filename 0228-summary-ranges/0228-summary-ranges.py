class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                ranges.append(self.get_output(start, nums[i-1]))
                start = nums[i]
        
        ranges.append(self.get_output(start, nums[-1]))
        return ranges

    def get_output(self, a, b):
        return f'{a}->{b}' if a != b else f'{a}'
