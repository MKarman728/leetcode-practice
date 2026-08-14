# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list1 = head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list2 = slow.next
        slow.next = None
        list2 = self.reverse(list2)
        while list2:
            next1 = list1.next
            next2 = list2.next
            list1.next = list2
            list1.next.next = next1
            list1= next1
            list2= next2

    
    def reverse(self, node):
        prev = None
        curr = node
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
