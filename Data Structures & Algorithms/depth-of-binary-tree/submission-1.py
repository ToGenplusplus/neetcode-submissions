# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: Optional[TreeNode], currDepth: int):
            if not node:
                return 0

            self.res = max(self.res, currDepth)
            dfs(node.left, currDepth + 1)
            dfs(node.right, currDepth + 1)

        dfs(root, 1)
        return self.res

            
