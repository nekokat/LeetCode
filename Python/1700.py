"""
1700. Number of Students Unable to Eat Lunch  https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
"""

from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = deque(students)
        while sandwiches and s and sandwiches[0] in s:
            if s[0] == sandwiches[0]:
                del s[0]
                sandwiches.pop(0)
            else:
                s.rotate(1)
        return len(s)
      
