"""
404. Sum of Left Leaves https://leetcode.com/problems/sum-of-left-leaves/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = list()
        def leftleaf(root: Optional[TreeNode], position: bool) -> None:
            if root:
                if position and root.left is None and root.right is None:
                    res.append(root.val)
                else:
                    if root.left:
                        leftleaf(root.left, True)
                    if root.right:  
                        leftleaf(root.right, False)
        leftleaf(root, False)   
        return sum(res)
