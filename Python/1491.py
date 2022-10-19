"""
1491. Average Salary Excluding the Minimum and Maximum Salary https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
"""


class Solution:
    def average(self, salary: List[int]) -> float:
        s = sorted(salary)[1:-1]
        return sum(s)/len(s)
