# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prevGroup = ListNode(0, head)
        while True:
            kth = prevGroup
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            nextGroup = kth.next
            prev, curr = nextGroup, prevGroup.next
            while curr != nextGroup:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            newTail = prevGroup.next
            prevGroup.next = kth
            prevGroup = newTail