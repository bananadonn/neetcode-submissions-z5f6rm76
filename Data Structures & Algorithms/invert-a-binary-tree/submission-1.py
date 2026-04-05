# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root)
        return root
    def dfs(self, curr):
        if not curr:
            return None
        left = curr.left
        right = curr.right
        curr.right = left
        curr.left = right
        self.dfs(curr.left)
        self.dfs(curr.right)
        