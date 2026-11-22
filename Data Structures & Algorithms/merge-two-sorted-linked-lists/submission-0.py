# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        p1 = list1
        p2 = list2

        res = resHead = ListNode(p1.val)
        if p1.val <= p2.val:
            res = resHead = ListNode(p1.val)
            p1 = p1.next
        else:
            res = resHead = ListNode(p2.val)
            p2 = p2.next
        while p1 and p2:
            #print('in loop')
            if p1.val <= p2.val:
                res.next = ListNode(p1.val)
                p1 = p1.next
            else:
                res.next = ListNode(p2.val)
                p2 = p2.next
            res = res.next
        if p1:
            res.next = p1
        if p2:
            res.next = p2
        return resHead

        #Trying in place
        # while p1.next and p2.next:
        #     t1 = p1.next
        #     t2 = p2.next
        #     if p1.val <= p2.val and t1.val >= t2.val:
        #         p1.next = p2
        #         p2.next = t1
        #         p1 = t1
        #         p2 = t2
        #     elif p2.val <= p1.val and t2.val >= t1.val:
        #         p2.next = p1
        #         p1.next = t2
        #         p1 = t1
        #         p2 = t2
        #     else:
        #         p1 = t1
        #         p2 = t2
        # return list2
