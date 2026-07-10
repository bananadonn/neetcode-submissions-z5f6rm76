# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxx = -1001
        typemax = self.bestoutput(root)
        return max(typemax, self.maxx)

    def bestoutput(self, curr):
        if not curr.left:
            left = 0
        else:
            left = self.bestoutput(curr.left)
        if not curr.right:
            right = 0
        else:
            right = self.bestoutput(curr.right)

        self.maxx = max(self.maxx, curr.val + left + right, curr.val)
        return max(curr.val + left, curr.val + right, curr.val)
        