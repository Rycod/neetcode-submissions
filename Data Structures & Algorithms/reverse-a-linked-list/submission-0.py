# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        old_h = head
        curr = head
        prev, temp = None, None
        while curr:
            if not curr.next:
                head = curr
            curr = curr.next
        curr = old_h
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return head
