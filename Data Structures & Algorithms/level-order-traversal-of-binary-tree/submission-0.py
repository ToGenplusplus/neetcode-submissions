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


        result = []
        q = deque([root])

        while q:
            # snapshot: get the number of nodes in the current level (# of nodes currenlt in queue)
            num_nodes_in_level = len(q)
            curr_level_vals = []

            # iterate through the nodes in the queue until
            # we have processed the num nodes = to num node in the level
            for _ in range(num_nodes_in_level):
                # remove the node in the left side of the queue
                curr = q.popleft()
                # insert its value into curr_level_vals
                curr_level_vals.append(curr.val)
                # if left node is not null add to q
                if curr.left:
                    q.append(curr.left)
                # if right node is not null add to q
                if curr.right:
                    q.append(curr.right)

            result.append(curr_level_vals)
        return result


        
        