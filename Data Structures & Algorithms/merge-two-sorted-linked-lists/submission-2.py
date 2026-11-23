# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = r1 = list1
        l2 = r2 = list2
        new = h = ListNode()
        while r1 and r2:
            if r1.val < r2.val:
                new.next = r1
                r1 = r1.next
            else:
                new.next = r2
                r2 = r2.next
            new = new.next
        if r1:
            new.next = r1
        if r2:
            new.next = r2
        return h.next
