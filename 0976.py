"""
976. Largest Perimeter Triangle https://leetcode.com/problems/largest-perimeter-triangle/
"""


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return sum(nums[i:i+3])
        return 0
        
