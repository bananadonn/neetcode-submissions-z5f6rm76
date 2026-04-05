# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)
        

    def traverse(self, curr):
        if not curr:
            return 0
        return 1 + max(self.traverse(curr.left), self.traverse(curr.right))
