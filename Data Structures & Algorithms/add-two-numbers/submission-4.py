# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode(0)
        carry = 0
        while l1 and l2 or carry:
            curr.next = ListNode()
            curr = curr.next
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            res = l1.val + l2.val + carry
            curr.val = res % 10
            carry = res // 10
            l1 = l1.next
            l2 = l2.next
        curr.next = l1 or l2
        return head.next
        