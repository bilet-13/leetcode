class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
           # backtrack, input argrment cur_str, cur_idx
        
        word_set = set(wordDict)

        @cache
        def dfs(start):

            if start == len(s):
                return [""]

            result = []

            for end in range(start + 1, len(s) + 1):
                prefix = s[start : end]

                if prefix in word_set:
                    sub_sentences = dfs(end)

                    for sub in sub_sentences:
                        if sub == "":
                            result.append(prefix)
                        else:
                            result.append(prefix + " " + sub)

            return result

        return dfs(0)
        