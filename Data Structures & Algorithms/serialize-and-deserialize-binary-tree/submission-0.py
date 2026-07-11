# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.serial = ""
        self.dfs(root)
        return self.serial[1:]

    def dfs(self, curr):
        if not curr:
            self.serial += (",None")
            return
        
        self.serial += ","
        self.serial += (str(curr.val))
        self.dfs(curr.left)
        self.dfs(curr.right)
        
        return
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.data = data.split(",")
        return self.dfs2()

    def dfs2(self):
        val = self.data.pop(0)
        if val == "None":
            return
        curr = TreeNode(int(val))
        curr.left = self.dfs2()
        curr.right = self.dfs2()

        return curr
