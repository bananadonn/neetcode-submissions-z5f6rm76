# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traverse(p,q)
        
    def traverse(self, p,q):
        if not p or not q:
            if p or q:
                return False
            return True
        if p.val != q.val:
            return False
        return self.traverse(p.left, q.left) and self.traverse(p.right , q.right)
        