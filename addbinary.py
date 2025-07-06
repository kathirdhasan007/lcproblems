class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary_ans = ""
        ans = int(a , 2) + int(b, 2)
        binary_ans = bin(ans)[2:]
        return str(binary_ans)
    
a = "1010"
b = "1011"
out = Solution()
print(out.addBinary(a,b))