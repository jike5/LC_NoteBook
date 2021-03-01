class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1.extend(nums2)
        nums1.sort()
        L = len(nums1)
        if L %2 == 0:
            ans = (nums1[L/2] + nums1[num1s/2 + 1])/2
        else:
            ans = nums1[int(L/2)]
        return ans


A = Solution()
print(A.findMedianSortedArrays([1,2],[3]))