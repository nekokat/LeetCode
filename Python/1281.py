"""
1281. Subtract the Product and Sum of Digits of an Integer  https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""

from operator import mul, add
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(map(int,str(n)))
        return reduce(mul, n) - reduce(add, n) 
        
        
