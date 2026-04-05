# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0

        def bfs(curr, l, h):
            if not curr:
                return

            bfs(curr.left, l, h)
            bfs(curr.right, l, h)
        
            if curr.val >= l and curr.val <= h:
                self.total += curr.val
        
        bfs(root, low, high)
        return self.total