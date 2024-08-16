class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [f'{nums[0]}']
        ranges = []
        a = nums[0]
        num_next = 0

        for i in range(1, len(nums)):
            if nums[i] != a + num_next + 1:
                ranges.append(self.get_output(a, a+num_next))
                a = nums[i]
                num_next = 0
            else:
                num_next += 1
            
            if i == len(nums) - 1:
                ranges.append(self.get_output(a, a+num_next))
                
        return ranges
    def get_output(self, a, b):
        return f'{a}->{b}' if a != b else f'{a}'
