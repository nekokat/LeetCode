"""
458. Poor Pigs  https://leetcode.com/problems/poor-pigs/submissions/
"""

from math import ceil, log

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets, minutesToTest/minutesToDie + 1))
