class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        a = 0
        b = 0
        ans = len(nums) + 1
        while b < len(nums):
            while sum(nums[a:b+1]) >= target:
                ans = min(ans, b-a+1)
                a += 1
            b += 1
        if ans == len(nums) + 1:
            return 0
        else:
            return ans

A = Solution()
print(A.minSubArrayLen(15, [1,2,3,4,5]))