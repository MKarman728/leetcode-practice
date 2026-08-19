# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.findHeight(root) != -1
    
    def findHeight(self, node):
        if not node:
            return 0
        left = self.findHeight(node.left)
        if left == -1:
            return -1
        right = self.findHeight(node.right)
        if right == -1:
            return -1 
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)