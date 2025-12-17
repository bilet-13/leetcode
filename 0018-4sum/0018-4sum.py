class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                cur_sum = nums[i] + nums[j]

                remain = target - cur_sum

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    sum_two = nums[left] + nums[right]

                    if sum_two == remain:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        right -= 1
                        left += 1

                    elif sum_two < remain:
                        left += 1

                    else:
                        right -= 1
            
        return [[n1, n2, n3, n4] for n1, n2, n3, n4 in result]

        