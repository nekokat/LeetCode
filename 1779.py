"""
1779. Find Nearest Point That Has the Same X or Y Coordinate    https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
"""


class Solution:
    def distance(self, x: int, y: int, point: List[int]) -> int:
        return abs(x-point[0]) + abs(y-point[1])
    
    def validation(self, x: int, y: int, points: List[List[int]]) -> List[List[int]]:
        return filter(lambda k: x == k[1][0] or y == k[1][1], enumerate(points))
    
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        return min(self.validation(x, y, points), key=lambda k: self.distance(x, y, k[1]), default = (-1,))[0]
        
        
