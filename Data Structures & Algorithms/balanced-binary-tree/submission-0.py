# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
            at each node 
                get the height of the left subtree
                get the height of the right subtree
                caluclate the difference
                    if > 1
                        return false
        """
        if not root:
            return True

        def findH(node):
            if not node:
                return (0, True)
        
            left = findH(node.left)
            right = findH(node.right)

            if not left[1] or not right[1]:
                return (0, False)

            difference = abs(left[0] - right[0])
            if difference > 1:
                return (0, False)
            return (1 + max(left[0], right[0]), True)
        
        result = findH(root)
        return result[1]