# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
            node, h_left, h_right, abs <= 1, returned height
            4, 0, 0, true, 1
            3, 1,0, true, 2
            2, 0,0, true, 1
            1, 1, 2, true, 3 -> true
        """

        def get_height(node: Optional[TreeNode]) -> (int, boolean):
            if not node:
                return (0,True)

            left_height, left_balanced = get_height(node.left)
            right_height, right_balanced = get_height(node.right)

            is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            return (1 + max(left_height, right_height), is_balanced)

        height, is_balanced = get_height(root)
        return is_balanced

        