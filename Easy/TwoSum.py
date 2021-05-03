"""https://leetcode.com/problems/two-sum/"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i]+nums[j] == target:
                        out=[]
                        out.append(i)
                        out.append(j)
                        return (out)