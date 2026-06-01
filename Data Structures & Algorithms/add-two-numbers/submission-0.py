# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        remainder = 0

        while l1 or l2 or remainder > 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            curr.next = ListNode((remainder + v1 + v2) % 10)
            remainder = (remainder + v1 + v2) // 10
            print(remainder)
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

            curr = curr.next
        
        return dummy.next
            

