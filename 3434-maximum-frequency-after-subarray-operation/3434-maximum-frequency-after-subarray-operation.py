class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # dp?
        # dp[i][j]: the maximum frequencey of any number of the subarr[i: j]
        # brute force
        # two for loop for i  and for j , count the number of max frequency val
        # 

        # time complexity o(V* len(nums))

        num_indices = defaultdict(list)
        n = len(nums)
        k_count_so_far = [0 for _ in range(n + 1)]

        for i in range(n):
            num_indices[nums[i]].append(i)
            k_count_so_far[i + 1] = k_count_so_far[i] + (1 if nums[i] == k else 0)

        max_profit = 0
        for num, indices in num_indices.items():
            if num == k:
                continue
            profit = 1
            cur = 1
            prev = indices[0]

            for i in range(1, len(indices)):
                cur -= k_count_so_far[indices[i]] - k_count_so_far[prev] 
                cur = max(0, cur)

                cur += 1 

                profit = max(profit, cur)
                prev = indices[i] 

            max_profit = max(max_profit, profit)
        
        return len(num_indices[k]) + max_profit

            






        