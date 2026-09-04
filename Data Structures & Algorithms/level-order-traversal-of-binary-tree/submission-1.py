from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        """
            use queue 
            start with root node
            iterate while there are nodes in the queue
            get snpashot of the number of items in the queue - n - these are the nodes in the current level
            of the tree
            iterate over the q items 10 times
                add the node.val to level array
                if node.left
                    add node.left to the queue (node a.ppend)
                if node.right
                    add node.right

        """

        q = deque([root])
        result = []

        while q:
            level_values = []
            num_nodes = len(q)
            for _ in range(num_nodes):
                node = q.popleft()
                level_values.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level_values)
        
        return result



        
        