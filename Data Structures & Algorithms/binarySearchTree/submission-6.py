class TreeNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key,val)
        curr = self.root
        
        if not self.root:
            self.root = newNode
            return
        
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = newNode
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = newNode
                    return
                curr = curr.right
            else:
                curr.val = newNode.val
                return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1


    def getMin(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val


    def remove(self, key: int) -> None:
        
        self.root = self.deleter(self.root, key)

    def deleter(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key < root.key:
            root.left = self.deleter(root.left, key)
        elif key > root.key:
            root.right = self.deleter(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                last = self.getmin(root.right)
                root.key = last.key
                root.val = last.val
                root.right = self.deleter(root.right, last.key)
        return root

    def getmin(self, root) -> TreeNode:
        if not root:
            return None
        while root and root.left:
            root = root.left
        return root


    def getInorderKeys(self) -> List[int]:
        keylist = []
        if not self.root:
            return []
        self.traversal(self.root, keylist)
        return keylist

    def traversal(self, root, arr) -> None:
        if not root:
            return
        self.traversal(root.left, arr)
        arr.append(root.key)
        self.traversal(root.right, arr)
