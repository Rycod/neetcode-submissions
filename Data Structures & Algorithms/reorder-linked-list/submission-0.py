# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        #Find midpoint
        s, f = head, head.next
        while f and f.next:
            f = f.next.next
            s = s.next
        second = s.next

        #Detach halves and reverse Second half
        s.next = None
        prev = None
        curr = second
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # prev now holds head of reversed second half

        #Merging both halves
        fcurr = head
        scurr = prev
        #second half will always be <= first, so use second for loop
        while scurr:
            ftmp = fcurr.next
            stmp = scurr.next
            fcurr.next = scurr
            fcurr = ftmp
            scurr.next = fcurr
            scurr = stmp