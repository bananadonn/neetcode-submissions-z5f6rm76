# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = []
        self.traversal(root, elements)
        return elements[k - 1]
    
    def traversal(self, root: Optional[TreeNode], elements: List[int]) -> None:
        if not root:
            return None
        self.traversal(root.left, elements)
        elements.append(root.val)
        self.traversal(root.right, elements)