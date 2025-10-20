class Solution:
    def reverseBits(self, n: int) -> int:
        reverseNum = 0

        for i in range(32):
            last_bit = n & 1
            n = n >> 1

            reverseNum = reverseNum << 1
            reverseNum |= last_bit

        return reverseNum
        