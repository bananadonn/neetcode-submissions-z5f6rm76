class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key 
        self.val = val
        self.next = None
    
class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
    
    def Hash(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.Hash(key)
        if not self.table[index]:
            self.table[index] = Node(key, value)
        else:
            node = self.table[index]
            prev = None
            while node:
                if node.key == key:
                    node.val = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
        
        self.size += 1
        if self.size >= (self.capacity * (0.5)):
            self.resize()

    def get(self, key: int) -> int:
        index = self.Hash(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.Hash(key)
        node = self.table[index]
        prev = None

        while node:
            if node.key == key:
                if not prev:
                    self.table[index] = node.next
                else:
                    prev.next = node.next
                self.size -= 1
                return True
            prev, node = node, node.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        newtable = [None] * self.capacity

        for node in self.table:
            while node:
                index = self.Hash(node.key)
                if not newtable[index]:
                    newtable[index] = Node(node.key, node.val)
                else:
                    nextnode = node.next
                    node.next = newtable[index]
                    newtable[index] = node
                    node = nextnode
                node = node.next
        self.table = newtable
            

