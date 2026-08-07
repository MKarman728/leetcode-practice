# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        prev = None
        l1_stack = []
        while curr:
            l1_stack.append(curr.val)
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        curr = l2
        prev = None
        l2_stack = []
        while curr:
            l2_stack.append(curr.val)
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        l1_stack.reverse()
        l1_string_result = "".join(str(num) for num in l1_stack)
        l1_num = int(l1_string_result)

        l2_stack.reverse()
        l2_string_result = "".join(str(num) for num in l2_stack)
        l2_num = int(l2_string_result)
        result = l1_num + l2_num
        print(result)
        result_array = [int(char) for char in str(result)]
        head = dummy = ListNode(0)
        print(result_array)
        for i in range(len(result_array)-1, -1, -1):
            dummy.val = result_array[i]
            if i - 1 >= 0:
                next = ListNode(None)
                dummy.next = next
                dummy = dummy.next
        return head
