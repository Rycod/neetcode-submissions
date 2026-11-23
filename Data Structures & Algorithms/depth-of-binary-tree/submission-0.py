# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        currDepth = 0
        def countDepth(root, currDepth):
            nonlocal maxDepth
            if not root:
                maxDepth = max(currDepth, maxDepth)
                return
            countDepth(root.left, currDepth+1)
            countDepth(root.right, currDepth+1)
        countDepth(root, currDepth)
        return maxDepth
            