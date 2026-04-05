# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        target = subRoot.val
        nodes = set()
        self.dfs(root,target,nodes)
        for node in nodes:
            print(self.samecheck(node,subRoot))
            if self.samecheck(node, subRoot):
                return True
        return False

    
    def samecheck(self, root, subRoot) -> bool:
        if not root or not subRoot:
            if root or subRoot:
                return False
            return True
        if root.val != subRoot.val:
            return False
        return self.samecheck(root.left, subRoot.left) and self.samecheck(root.right, subRoot.right)
    
    def dfs(self, root, target, nodes):
        if not root:
            return
        if root.val == target:
            nodes.add(root)
        self.dfs(root.left, target, nodes)
        self.dfs(root.right, target, nodes)
        return nodes