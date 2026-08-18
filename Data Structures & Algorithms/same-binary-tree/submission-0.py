# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = deque()
        tree1.append(p)

        tree2 = deque()
        tree2.append(q)
        while tree1:
            node1 = tree1.popleft()
            node2 = tree2.popleft()
            if node1 and node2 and node1.val != node2.val:
                return False
            elif node1 and not node2 or not node1 and node2:
                return False
            if isinstance(node1, TreeNode):
                tree1.append(node1.left)
                tree1.append(node1.right)
            if isinstance(node2, TreeNode):
                tree2.append(node2.left)
                tree2.append(node2.right)
        return True