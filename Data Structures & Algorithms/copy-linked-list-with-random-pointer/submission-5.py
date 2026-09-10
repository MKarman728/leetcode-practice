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
        if head is []:
            return []
        old_to_new = {None: None}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        curr2 = head
        while curr2:
            old_to_new[curr2].next = old_to_new[curr2.next]
            old_to_new[curr2].random = old_to_new[curr2.random]
            curr2 = curr2.next
        return old_to_new[head]