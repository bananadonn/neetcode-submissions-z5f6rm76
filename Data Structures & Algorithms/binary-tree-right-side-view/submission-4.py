# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        view = []
        if root:
            q.append(root)
            view.append(root.val)
        while q:
            num = None
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    num = curr.left.val
                if curr.right:
                    q.append(curr.right)
                    num = curr.right.val
            if num:
                view.append(num)
        return view