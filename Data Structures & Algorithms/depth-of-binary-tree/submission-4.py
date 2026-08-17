# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append((root, 1))
        res = 0
        while queue:
            node, value = queue.popleft()
            res = max(res, value)
            if node.left:
                queue.append((node.left, value + 1))
            if node.right:
                queue.append((node.right, value + 1))
        return res