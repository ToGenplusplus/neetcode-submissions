# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    result = 0

    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return self.result

        def dfs(node: TreeNode, max_before):
            
            if node.val >= max_before:
                self.result += 1
                max_before = node.val
            
            if node.left:
                dfs(node.left, max_before)
            if node.right:
                dfs(node.right, max_before)

        dfs(root, float('-inf'))
        return self.result

        """
            [3,3,null,4,2]
            3,-inf
                3 > -inf, good += 1 = 1
                    left, 3, 3
                        3 = 3
                        left, 4, 3
                            4 > 3 , good += 1 = 2
                        right, 2,3
                            2 < 3
        """  
