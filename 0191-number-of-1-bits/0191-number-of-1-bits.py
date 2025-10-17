class Solution:
    def hammingWeight(self, n: int) -> int:
        num_one_bit = 0

        while n != 0:
            last_bit = n & 1
            n = n >> 1
            
            num_one_bit += last_bit 
        return num_one_bit 