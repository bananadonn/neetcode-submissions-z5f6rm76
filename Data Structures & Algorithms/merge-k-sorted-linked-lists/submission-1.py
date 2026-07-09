# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-10001,None)
        for l in lists:
            self.merge2lists(dummy, l)
        
        return dummy.next
        
    def merge2lists(self, a, b):
        head = ListNode(-1001, None)
        temp = head
        while a and b:
            if a.val <= b.val:
                temp.next = a
                temp = a
                a = a.next
            else:
                temp.next = b
                temp = b
                b = b.next
        if b and not a:
            temp.next = b
        elif a and not b:
            temp.next = a
        
        return head.next
        



        