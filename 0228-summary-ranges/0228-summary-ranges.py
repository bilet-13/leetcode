class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        a = None
        num_next = 0

        for i in range(0, len(nums)):
            if a == None:
                a = nums[i]
                num_next = 0

            elif nums[i] != a + num_next + 1:
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
