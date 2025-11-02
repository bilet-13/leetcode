class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strict prefix? like bat is not the strict prefix of bat
        # normal prefix
        commonPrefix = strs[0]

        for i in range(1, len(strs)):
            commonPrefix = commonPrefix[:min(len(commonPrefix), len(strs[i]))]

            for j in range(len(commonPrefix)):
                if strs[i][j] != commonPrefix[j]:
                    commonPrefix = commonPrefix[:j]
                    break

        return commonPrefix
        