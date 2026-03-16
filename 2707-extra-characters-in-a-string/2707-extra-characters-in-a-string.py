class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
         # memo dp?
        # input argument: cur_idx
        # how to make extra char?
        n = len(s)
        words = set(dictionary)

        @cache
        def dp(cur_idx):
            if cur_idx == n:
                return 0

            # skip the current char
            min_extra_char_result = 1 + dp(cur_idx + 1) 

            for i in range(cur_idx + 1, n + 1):
                sub_str = s[cur_idx: i]

                if sub_str in  words:
                    min_extra_char_result = min(min_extra_char_result, dp(i))

            return min_extra_char_result

        return dp(0)

        
        
        