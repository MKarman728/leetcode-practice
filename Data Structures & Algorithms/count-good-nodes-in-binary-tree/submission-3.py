# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node, maxVal):
            if node.val >= maxVal:
                self.count += 1
            newMaxVal = max(node.val, maxVal)
            if node.left:
                dfs(node.left, newMaxVal)
            if node.right:
                dfs(node.right, newMaxVal)
        dfs(root, root.val)
        return self.count