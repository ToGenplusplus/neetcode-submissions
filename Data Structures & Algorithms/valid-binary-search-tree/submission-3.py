# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
            max(node.left) < node.val < min(node.right)

            top down
                at each node we need to know.
                    if its > than its low and < than its high

                root, float(-inf), -inf
                    valid
                    left subtree, nodes must be less than previous, so previous is high
                    left(1), -inf, root.val(2)
                        true
                    right subtree, nodes must be > than previous, so previous is low
                    right(3), root.val(2), inf
                        2 < 3 < inf - true
                        left(0), low(2)  high(3)
                        0 is not > 2 - false
        """

        def dfs(node, low, high) -> bool:
            if not node:
                return True

            is_val = low < node.val < high
            if not is_val:
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float('-inf'), float('inf'))