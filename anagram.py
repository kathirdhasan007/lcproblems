class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        answer = True
        if sorted(s) == sorted(t):
            return True
        else:
            return False

s = "silent"
t = "listen"
out = Solution()
print(out.isAnagram(s,t))