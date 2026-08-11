# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1: 
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if i + 1 < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2=None
                mergedList  = self.mergeTwoLists(list1, list2)
                merged.append(mergedList)
            lists = merged
        return lists[0]
        
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        res = curr = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        curr.next = list1 or list2
        return res.next