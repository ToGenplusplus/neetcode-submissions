# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        curr = root

        # iterate while there are still elements in stack or curr is not none
        while stack or curr:

            #traverse down the left of tree to the left most element (minimum)
            while curr:
                stack.append(curr)
                curr = curr.left
            

            # remove the element from the top of the stack
            # reduce our k - 1
            # if k == 0, we found our result
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            # move to the right element
            curr = curr.right

        return -1
