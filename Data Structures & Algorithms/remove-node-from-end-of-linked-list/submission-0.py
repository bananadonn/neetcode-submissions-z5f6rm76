# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, head

        for i in range(n - 1):
            first = first.next

        if not first.next:
            return head.next

        while first.next.next:
            second = second.next
            first = first.next
        
        second.next = second.next.next

        return head
        