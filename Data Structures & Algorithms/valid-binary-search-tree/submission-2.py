# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        #returns (bool, min, max)
        def get_min_max(node: Optional[TreeNode]):

            if not node:
                return (True, float('inf'), float('-inf'))

            invalid = (False, None, None)

            left_valid, left_min, left_max = get_min_max(node.left)
            right_valid, right_min, right_max = get_min_max(node.right)

            if not left_valid or not right_valid:
                return invalid

            if (left_max >= node.val) or (right_min <= node.val):
                return invalid

            return (True, min(left_min, node.val), max(right_max, node.val))

        result = get_min_max(root)
        return result[0]
        
        """
        root = [2,1,3]
         2.left is 1 < 2 -> true
         2.right is 3 > 2 -> true
        root = [5,1,3]
         2.left is 5 > 2 -> false

        v1
         at a node we need to know
            is this node on the left of its parent
                yes
                    is its value < than its parent value?
                        yes -> true
                        no -> false
                no
                    is its value > than its parent value
                        yes -> true
                        no -> false


         at a node we need to know 
            if its minimum value in the right subtree is < than node.val
            if its maximum value in the left subtree is > than node.val


            node is null, return (None, None)

            (min,max, bool)
            left = get_min_max(node.left)
            right = get_min_max(node.right)
            if left[1] >= node.val -> false
            if right[0] <= node.val -> false

            return min(left[0],node.val), max(right[1], node.val)


        


        """