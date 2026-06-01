"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old = head 
        ans = Node(0)
        curr = ans

        #build list with only nxt ptr
        while old:
            newnode = Node(old.val)
            curr.next = newnode
            curr = curr.next
            old = old.next
        
        #go back to beginning
        old = head
        curr = ans.next

        while old:
            pos = head
            pos2 = ans.next
            random = old.random
            while pos != random:
                if pos == None:
                    pos2 = None
                    break
                pos = pos.next
                pos2 = pos2.next
            curr.random = pos2
            curr = curr.next
            old = old.next
        return ans.next

                

        
        