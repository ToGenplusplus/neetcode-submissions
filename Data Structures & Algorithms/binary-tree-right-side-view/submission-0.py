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

        result = []
        q = deque([root])

        while q:
            num_nodes_in_level = len(q)
            last_node = None

            for _ in range(num_nodes_in_level):
                last_node = q.popleft()
                if last_node.left:
                    q.append(last_node.left)
                if last_node.right:
                    q.append(last_node.right)
            
            # safety check
            if last_node:
                result.append(last_node.val)
        return result

        """
            given:
                root of a binary search tree
            return:
                list of values on the right side of the tree, aranged from top to bottom

            examples


            clairfications:
                how large can this tree be?
                are there time and space complexity constraints?

                list of values that are VISIBLE from the right side of the tree (consider example 2)

            root is always visible
            a node is included in its result if there is no other node to the right on the same level

            need to keep track of which level a node is on
            need a way to keep track of whether a node is the right most node on the same level


            we can use the binary tree level order traversal with level tracking to determine the level
            the node belongs to
            the last node on the level will then get added to the result list 
            the last node will always be the right most node
        """