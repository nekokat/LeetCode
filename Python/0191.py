"""
191. Number of 1 Bits https://leetcode.com/problems/number-of-1-bits/
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return "{:b}".format(n).count("1")
