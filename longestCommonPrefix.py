class Solution:
    def longestCommonPrefix(self, strs: list[str]) ->str:
        if not strs:
            return ""

        prefix= strs[0]
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

            
strs = ["flower","flow","flight"]
out = Solution()
print(out.longestCommonPrefix(strs))