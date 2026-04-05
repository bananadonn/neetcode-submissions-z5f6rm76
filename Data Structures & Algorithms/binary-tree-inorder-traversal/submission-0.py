# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.traversal(root, arr)
        return arr
    def traversal(self, root: Optional[TreeNode], arr: List[int]) -> None:
        if not root:
            return None
        self.traversal(root.left, arr)
        arr.append(root.val)
        self.traversal(root.right, arr)