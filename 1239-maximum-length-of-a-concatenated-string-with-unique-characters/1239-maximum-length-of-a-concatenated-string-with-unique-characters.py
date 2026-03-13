class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # backtracking 
        # find maximum -> DP -> bit mask?

        # only focus on backtracking
        # input argrmemtn: start_idx: the cur_idx of arr, 
        unique_arr = []

        for s in arr:
            if len(s) != len(set(s)):
                continue

            unique_arr.append(s) 

        str_mask = []
        for s in unique_arr:
            mask = 0
            for char in s:
                mask |= (1 << ord(char) - ord('a'))

            str_mask.append(mask)


        used_chars = set()
        max_length = 0
        n = len(unique_arr)

        @cache
        def dp(mask, start_idx):
            if mask.bit_count() == 26 or start_idx == n:
                return 0

            max_len = 0

            for i in range(start_idx, n):

                if mask & str_mask[i] != 0:
                    continue
                
                max_len = max(max_len, len(unique_arr[i]) + dp(mask | str_mask[i], i + 1))

            return max_len
                
        return dp(0, 0)




        