class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k's range 1 - max(piles)
        # and the condition look like x x x x o o o o and we want to find the leftmost o that is minimum one
        # binary seach
        # time complexity o(len(piles) * log(max(piles)))

        def can_eat(k):
            time = 0
            for p in piles:
                while p > 0:
                    p -= k
                    time += 1
                    if time > h:
                        return False
            
            return time <= h

        left = 1
        right = max(piles)

        while left <= right:
            k = (left + right) // 2

            if can_eat(k):
                right = k - 1
            else:
                left = k + 1
        
        return left
        