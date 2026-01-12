class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            s = strs[i]

            new_prefix = ""
            for j in range(min(len(prefix), len(s))):
                if prefix[j] != s[j]:
                    break

                new_prefix += prefix[j]
            prefix = new_prefix

        return prefix
        