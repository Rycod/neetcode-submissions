# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listlen = 0
        curr = head
        while curr:
            curr = curr.next
            listlen += 1
        if listlen - n == 0:
            head = head.next
            return head
        
        n = listlen - n
        i = 0
        curr = head
        prev = curr
        while i < n:
            i += 1
            prev = curr
            curr = curr.next
        
        prev.next = curr.next

        
        print(i, curr.val)
        return head