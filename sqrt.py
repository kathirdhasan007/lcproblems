import math
class Solution:

    def mySqrt(self, x: int) -> int: 
        ans = math.sqrt(x)
        return int(ans)
    
x = 4
out = Solution()
print(out.mySqrt(x))