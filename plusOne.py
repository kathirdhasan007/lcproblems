class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        join_word= "".join(str(num) for num in digits)
        s = int(join_word)        
        ans = s + 1

        digit = []
        digit = [int(digit) for digit in str(ans)]
        return digit

digits = [1,2,3] 
out = Solution()
print(out.plusOne(digits))
