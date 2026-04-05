# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(node1, node2):
            if not node1 and not node2:
                return None
            
            if node1 and not node2:
                newnode = TreeNode(node1.val, helper(node1.left, None), helper(node1.right, None))
            elif node2 and not node1:
                newnode = TreeNode(node2.val, helper(None, node2.left), helper(None,node2.right))
            elif node1 and node2:
                newnode = TreeNode(node1.val + node2.val, helper(node1.left, node2.left), helper(node1.right,node2.right))
            return newnode
        
        return helper(root1, root2)