"""
1. Two Sum  https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i, j in enumerate(nums):
            k = target-j
            res.append(i)
            if k in nums and nums.index(k) != i:
                res.append(nums.index(k))
                break
        return res[-2::]
