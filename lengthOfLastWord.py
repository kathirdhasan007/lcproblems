class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        for i in s:
            sentence = word[-1]
            lenght = len(sentence)
            return lenght

s = "luffy is still joyboy"      
out = Solution()
print(out.lengthOfLastWord(s))