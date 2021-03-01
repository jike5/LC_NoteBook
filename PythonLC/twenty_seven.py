class Solution1:
    def removeElement(self, nums, val) -> int:
        i = 0
        ans = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(val)
                ans += 1
            else:
                i += 1
        return nums


# 双指针
class Solution2:
    def removeElement(self, nums, val) -> int:
        a = 0
        b = 0
        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b


A = Solution1()
# print(A.removeElement([0,1,2,2,3,0,4,2], 2))
print(A.removeElement([3,3,2,2],3))