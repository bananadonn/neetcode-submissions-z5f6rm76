# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        val = 0
        return self.pathhelper(root, targetSum, val)
    
    def pathhelper(self, root: Optional[TreeNode], target: int, val: int) -> bool:
        if not root:
            return False
        val += root.val

        if not root.left and not root.right and val == target:
            return True
        if self.pathhelper(root.left, target, val):
            return True
        if self.pathhelper(root.right, target, val):
            return True
        val -= root.val
        return False
        