# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q or not p:
            return (q is None) == (p is None)
        if q.val != p.val:
            return False
        q1 = deque([q])
        q2 = deque([p])
        # print(q.left)
        while q1 and q2:
            n1 = q1.pop()
            n2 = q2.pop()
            val1 = n1.val
            val2 = n2.val
            if val1 != val2:
                return False
            # print('Left:', n1.left is None, n2.left is None, '\nRight:', n1.right is None, n2.right is None)
            if ((n1.left is None) != (n2.left is None)) or ((n1.right is None) != (n2.right is None)):
                return False
            if n1.left and n2.left:
                q1.append(n1.left)
                q2.append(n2.left)
            if n1.right and n2.right:
                q1.append(n1.right)
                q2.append(n2.right)
        return False if q1 or q2 else True