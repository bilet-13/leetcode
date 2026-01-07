class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
           # brute force way 
        # try weight from 0 to 1 
        # return the lease weight that all package can be shiped

        # how to improve
        # use binary search to find answer
        # start_limit = 1
        # end_limit = sum of the weights / days?
        # time complexity o(WlogSum(weights))
        # x x x o <- need to find this elemnt o o

        start_limit = max(weights)
        end_limit = sum(weights)

        def can_load(max_weight):
            total_days = 1
            cur_load = 0

            for w in weights:
                if cur_load + w > max_weight:
                    total_days += 1 
                    cur_load = 0

                cur_load += w

            return total_days <= days

        while start_limit <= end_limit:
            cur_limit = (end_limit + start_limit) // 2

            if can_load(cur_limit):# the weight is enough , try lower it
                end_limit = cur_limit - 1 

            else:
                start_limit = cur_limit + 1

        return start_limit # the leash nu
        