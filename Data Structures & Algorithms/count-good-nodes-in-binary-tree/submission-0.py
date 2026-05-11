# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    num_good_nodes = 0

    def goodNodes(self, root: TreeNode) -> int:
        return self.findGoodNodes(root, root.val)
   

    def findGoodNodes(self, node: TreeNode, max_val: int) -> int:
        if not node:
            return 0

        count = 1 if node.val >= max_val else 0

        next_max_val = max(max_val, node.val)

        count += self.findGoodNodes(node.left, next_max_val)
        count += self.findGoodNodes(node.right, next_max_val)

        return count


        """
            given a binary tree (not a bst)

            return
                # of good nodes within the tree (in any order)
            
            examples

            constrainsts
            root cannot be null
            each node can have 0,1,2 children
            time and space complexity?

            Reasoning:
            since this is not a BST, we wil need to visit every node
            need a way to track the values of nodes in path from root to node x
            root is always a good node

            using example 2
            1 - good
            1.left = 2 > 1 - good
            2.left = 3 > 2 > 1 - good
            2.right = 4 > 2 > 1 - good

            need to keep track of the max value seen so far along a nodes path
            if the current node x.val is > than the max seen along the path from root to x
            we can add that node to result and update max seen before calling algo on node.left and node.right

        """