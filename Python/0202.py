"""
202. Happy Number https://leetcode.com/problems/happy-number/
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        while n not in [1, 4]:
            n = sum(map(lambda x: x*x, map(int, str(n))))
        return n == 1
