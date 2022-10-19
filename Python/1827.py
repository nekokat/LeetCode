"""
1827. Minimum Operations to Make the Array Increasing   https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                k = nums[i]-nums[i+1]+1
                nums[i+1] += k
                res += k
        return res
      
