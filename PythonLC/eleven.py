class Solution:
    def maxArea(self, height) -> int:
        max = 0
        a = 0
        b = len(height) - 1
        while a < b:
            cur = min(height[a], height[b])*(b - a)
            if cur > max:
                max = cur
            a += 1
            b -= 1
        return max 

A = Solution()
print(A.maxArea([1,8,6,2,5,4,8,3,7]))