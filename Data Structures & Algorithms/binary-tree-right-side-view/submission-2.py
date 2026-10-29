from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        """
            return the last node on each level

            approach is to do the level order traversal
            discard each node in a level until its the last node
            and the last node.val to result array
        """

        q = deque([root])

        result = []

        while q:
            num_nodes = len(q)

            for i in range(num_nodes):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if i == num_nodes - 1:
                    result.append(node.val)
        
        return result

