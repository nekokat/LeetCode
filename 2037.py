"""
2037. Minimum Number of Moves to Seat Everyone  https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
"""

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(i-j) for i, j in zip(sorted(seats),sorted(students)))
