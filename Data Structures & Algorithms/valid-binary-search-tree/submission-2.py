# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.dfs(root, -10001, 10001)

    def dfs(self, root, mini, maxx):
        if not root:
            return True
        if root.val <= mini or root.val >= maxx:
            return False

        return self.dfs(root.left, mini, root.val) and self.dfs(root.right, root.val, maxx)

        