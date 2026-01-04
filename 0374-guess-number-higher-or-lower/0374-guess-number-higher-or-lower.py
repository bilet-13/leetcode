# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
          # binary search
        # o(logn)
        left = 1
        right = n

        while left < right:
            mid = (right + left) // 2

            guess_result = guess(mid)

            if guess_result ==  1:
                left = mid + 1

            else:
                right = mid

        return left


        