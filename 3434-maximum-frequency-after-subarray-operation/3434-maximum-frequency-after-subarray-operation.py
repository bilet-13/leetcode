class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # dp?
        # dp[i][j]: the maximum frequencey of any number of the subarr[i: j]
        # brute force
        # two for loop for i  and for j , count the number of max frequency val
        # 

        # time complexity o(V* len(nums))

        counter = Counter(nums)
        result = 0
        k_num = counter[k] if k in counter else 0

        for num, count in counter.items():
          
            cur = 0
            max_profit = 0
            for i in range(len(nums)):
                cur = max(cur, 0)

                if nums[i] == k:
                    cur -= 1
                elif nums[i] == num:
                    cur += 1

                max_profit = max(cur, max_profit)

            result = max(result, max_profit + k_num) 

        return result

                    


