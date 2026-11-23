# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                # print("Returning")
                return
            # print("Processing R", root.val)
            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)
        # def printbfs(root):
        #     q = deque()
        #     q.append(root)
        #     level = 0
        #     while q:
        #         curr = q.popleft()
        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)
        dfs(root)
        # printbfs(root)
        return root