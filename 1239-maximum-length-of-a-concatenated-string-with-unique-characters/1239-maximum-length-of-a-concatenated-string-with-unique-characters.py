class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # backtracking 
        # find maximum -> DP -> bit mask?

        # only focus on backtracking
        # input argrmemtn: start_idx: the cur_idx of arr, 
        unique_arr = []

        for s in arr:
            if any(freq > 1 for _, freq in Counter(s).items()):
                continue

            unique_arr.append(s) 

        used_chars = set()
        max_length = 0
        n = len(unique_arr)

        def backtrack(start_idx, cur_len):
            nonlocal max_length
            
            max_length = max(max_length, cur_len)

            if start_idx == n:
                return

            for i in range(start_idx, n):
                if any(char in used_chars for char in unique_arr[i]):
                    continue # invalid string
                
                for char in unique_arr[i]:
                    used_chars.add(char)

                backtrack(i + 1, cur_len + len(unique_arr[i]))

                for char in unique_arr[i]:
                    used_chars.remove(char)
        
        backtrack(0, 0)
        return max_length




        