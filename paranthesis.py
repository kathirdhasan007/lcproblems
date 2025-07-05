class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(',']': '[', '}': '{'}

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False

s = "(]"
out = Solution()
print(out.isValid(s))