class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        hasGreatestCandies = []
        max_candies = max(candies)

        for num_candies in candies:
            hasGreatestCandies.append(num_candies + extraCandies >= max_candies)

        return hasGreatestCandies

