# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        input: root: [1,2,3,4,5,6,7] -> [1,3,2,7,6,5,4]

        basically at each node we swap its left and right children

        visit each node once
        3
        6 7
        3.left is not null
        r.right is not null
        tmp = 3.right
        3.right = 3.left
        3.left = temp
        return 3
        if we are at a leaf node
        7.left == null && 7.right == null
            return root
        else
            tmp = invertTree(root.right)
            root.right = invertTree(root.left)
            root.left = temp
            return root
        """
        if not root:
            return root
        tmp = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = tmp
        return root