"""
38. Count and Say https://leetcode.com/problems/count-and-say/
"""

import re

class Solution:
    def countAndSay(self, n: int) -> str: 
        dp = ["1","11","21","1211", "111221"]
        if n < len(dp):
            return dp[n-1]

        j = re.compile("(1+|2+|3+|4+|5+|6+|7+|8+|9+)")
        
        for i in range(len(dp), n):
            l = re.findall(j, dp[-1])
            dp.append("".join(f"{len(i)}{i[0]}" for i in l))
        return dp[n-1]
        
