# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = curr = ListNode(0, head)
        forward = head
        while n:
            forward = forward.next
            n -= 1
        while forward:
            curr = curr.next
            forward = forward.next
        curr.next = curr.next.next
        return dummy.next