"""https://leetcode.com/problems/median-of-two-sorted-arrays/"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        n = len(nums3)
        if n%2==0:
            k = n//2
            return (nums3[k]+nums3[k-1])/2
        else:
            k=n//2
            return nums3[k]