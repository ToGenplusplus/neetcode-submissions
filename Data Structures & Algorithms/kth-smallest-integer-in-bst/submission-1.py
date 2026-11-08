# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = -1

        if not root:
            return res

        in_order = []

        def traverse(node: TreeNode):
            nonlocal res
            if res != -1:
                return 

            if node.left:
                traverse(node.left)

            in_order.append(node.val)

            if len(in_order) == k:
                res = node.val
                return

            if node.right:
                traverse(node.right)

        traverse(root)

        return res
        
        """
        k = 3
            6
        3       7

    1       4 7

    ----

        6
            3
                1 - apend [1]
                len(io) = 1 < k
            append(3 to io) = [1,2]
            len(i0) = 2 < 3
            4 
                append (4) to io =[1,2,4]
                len(io) = 3 = k - res = 4 


        """