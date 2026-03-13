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

        used_chars = set()
        max_length = 0
        n = len(unique_arr)

        @cache
        def dp(mask, start_idx):
            if mask.bit_count() == 26 or start_idx == n:
                return 0

            max_len = 0

            for i in range(start_idx, n):
                is_duplicate = False

                for char in unique_arr[i]:
                    if mask & (1 << ord(char) - ord('a')) != 0:
                        is_duplicate = True
                        break

                if is_duplicate:
                    continue

                next_mask = mask
                for char in unique_arr[i]:
                    next_mask |= (1 << ord(char) - ord('a'))
                
                max_len = max(max_len, len(unique_arr[i]) + dp(next_mask, i + 1))

            return max_len
                
        return dp(0, 0)




        