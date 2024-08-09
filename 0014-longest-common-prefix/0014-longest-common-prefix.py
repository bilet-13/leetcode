class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for string in strs[1:]:
            if prefix == "" or string == "":
                prefix = ""
                break
            prefix = prefix[:min(len(prefix), len(string))]

            for i in range( min(len(string), len(prefix)) ):
                if string[i] != prefix[i]:
                    if i == 0:
                        prefix = ""
                        break
                    else:
                        prefix = prefix[:i]
                        break

        return prefix
