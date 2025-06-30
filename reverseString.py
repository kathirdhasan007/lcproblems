class Solution:
    def reverseString(self, s: list[str]) ->None:
        for i in s:
            s = s.reverse()
            return s
            

s = ["h","e","l","l","o"]
out = Solution()
print(out.reverseString(s))