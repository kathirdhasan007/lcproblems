class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    new = [i, j]
                    return new


nums = [2, 7, 11, 15]
target = 9
op = Solution()
print(op.twoSum(nums,target))
