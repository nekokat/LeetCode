"""
1329. Sort the Matrix Diagonally  https://leetcode.com/problems/sort-the-matrix-diagonally/
"""

import numpy as np

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        matrix = np.array(mat)
        n, m = len(mat), len(mat[0])
        
        for i in range(-n+1,m):
            l = sorted(np.diag(matrix, k=i))
            if i < 0:
                np.fill_diagonal(matrix[-i:], l)
            else:
                np.fill_diagonal(matrix[:,i:], l)
        return matrix
