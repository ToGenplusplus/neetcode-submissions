# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = None

        if not root:
            return res

        in_order = []

        def traverse(node: TreeNode):
            
            nonlocal res, k

            if not node or res:
                return 

            traverse(node.left)

            k -= 1
            if k == 0:
                res = node.val
                return

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