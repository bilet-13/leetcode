class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window
        # check the window contain t or not, use hash map to store the 
        # frequency 
        # the compare time is o(1) becasue the t only contain upper and lower english letter
        # 
        # if yes shrink the left window until the window does not contain t
        # use two var result_substring_start and result_substring_len to record the anser
        # update it during shringkinog
        # time complexity o(n)

        result_str_start = 0
        result_str_len = float('inf')

        count_t = Counter(t)
        cur_count = defaultdict(int)

        left = 0

        def contain_t(cur_count):
            return all(cur_count.get(char, 0) >= count for char, count in count_t.items())


        for right in range(len(s)):
            cur_count[s[right]] += 1

            while contain_t(cur_count) and left <= right:
                window_str_len = right - left + 1

                if window_str_len < result_str_len:
                    result_str_len = window_str_len
                    result_str_start = left

                cur_count[s[left]] -= 1
                left += 1
        
        return s[result_str_start: result_str_start + result_str_len] if result_str_len != float('inf') else "" 




        
        