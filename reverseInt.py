class Solution:
    def reverse(self, x: int) -> int:
        reverse_text = ""

        if x < 0:
            neg = -x
            for i in str(neg):
                reverse_text = i + reverse_text
            result = -int(reverse_text)      
        else:
            for i in str(x):
                reverse_text = i + reverse_text
            result = int(reverse_text)


        if result < -2**31 or result >2**31 - 1:
            return 0
        return result
x =-123
out = Solution()
print(out.reverse(x))