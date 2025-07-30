class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle[::1] in haystack[::1]:
            return haystack.index(needle)
        else:
            return -1





haystack = "sadbutnotsad"
needle = "sad"
out = Solution()
print(out.strStr(haystack,needle))