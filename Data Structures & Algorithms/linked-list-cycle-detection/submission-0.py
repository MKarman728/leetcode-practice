# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        obj = {}
        while head:
            if head in obj:
                return True
            else:
                obj[head] = 1
            head = head.next
        return False