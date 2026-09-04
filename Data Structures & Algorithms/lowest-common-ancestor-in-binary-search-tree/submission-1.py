# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: empty node, or we found either p or q
        if not root or root == p or root == q:
            return root

        # Search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both subtrees returned a non-null node, root is the LCA
        if left and right:
            return root

        # Otherwise, pass along whichever side found a target node
        return left if left else right
                
        """ 
        p = 3, q = 8
        node, is p or q
        2, no
        1, no,
        4, no
        7, no
        9, no
        3, yes
        8, yes
        5.left = yes
        5.right = yes so 5 is the LCA


        p = 3, q = 8
        node, is p or q
        2, no
        1, no
        4, yes
        3, yes, sice 3.right is also yes and we know p != q (distinct values) we can return 3 as the 
        LCA

        approach
        have a global variable to store the LCA
        traverse tree bottom up
            if node.left is yes and node.right is yes -> LCA is node
            if node = p or node = q and either (node.left is yes or node.right is yes) -> LCA is node


        """