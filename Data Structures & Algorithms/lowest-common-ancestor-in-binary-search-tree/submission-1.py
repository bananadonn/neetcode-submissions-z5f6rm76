# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        smal, big = min(p.val,q.val), max(p.val,q.val)

        while True:
            if root.val > big:
                root = root.left
            elif root.val < smal:
                root = root.right
            else:
                return root