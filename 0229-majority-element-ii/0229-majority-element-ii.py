class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
         # voting algo: find element that appear most
        
        num1, c1 = None, 0
        num2, c2 = None, 0
        
        for num in nums:
            if num == num1:
                c1 += 1
            
            elif num == num2:
                c2 += 1
            
            elif c1 == 0 or c2 == 0:
                if c1 == 0:
                    num1, c1 = num, 1
                else:
                    num2, c2 = num, 1
                
            else:
                c1 -= 1
                c2 -= 1

        return [n for n in [num1, num2] if nums.count(n) > len(nums) // 3]

        