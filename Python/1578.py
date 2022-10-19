"""
1578. Minimum Time to Make Rope Colorful    https://leetcode.com/problems/minimum-time-to-make-rope-colorful
"""


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        s = 0
        temp = []
        for position, colors in enumerate(zip(colors,colors[1::]+"*"),start=1):
            color, next_color = colors
            if not temp:
                temp.append(neededTime[position-1])
            if color == next_color:
                temp.append(neededTime[position])
            else:
                s += sum(temp) - max(temp, default=0)
                temp.clear()
        return s
