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
        cache = {None:None}
        if not head:
            return None
        curr = head
        while curr:
            cache[curr] = Node(curr.val)
            curr = curr.next
        curr2 = head
        while curr2:
            cache[curr2].next = cache[curr2.next]
            cache[curr2].random = cache[curr2.random]
            curr2 = curr2.next
        return cache[head]