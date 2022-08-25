"""
2373. Largest Local Values in a Matrix  https://leetcode.com/problems/largest-local-values-in-a-matrix/
"""

import numpy as np

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m = np.matrix(grid)
        rows = cols = range(1,len(grid)-1)
        
        def gererator(rows: range, cols: range) -> Generator[int, None, None]:
            for row in rows:
                for col in cols:
                     yield m[row-1:row+2:1,col-1:col+2:1].max()
                        
        return list(np.array(list(gererator(rows, cols))).reshape((max(rows), max(cols))))
        
        
        
