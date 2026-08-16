# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # Tail of the previous group
        groupPrev = dummy
        while True:
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            # first node of the next group
            groupNext = kth.next
            #first node here becomes tail
            groupHead = groupPrev.next
            kth.next = None
            groupPrev.next = self.reverse(groupHead)
            groupHead.next = groupNext
            groupPrev = groupHead


    
    def reverse(self, node: ListNode)->Optional[ListNode]:
        # returns head of reverse node
        prev  = None
        curr = node
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev