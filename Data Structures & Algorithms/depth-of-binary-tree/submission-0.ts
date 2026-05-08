/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    maxDepthFound: number = 0
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    maxDepth(root: TreeNode | null) {
        if (root === null) return 0
        this.findMaxDepth(root, 1)
        return this.maxDepthFound
    }

    findMaxDepth(node: TreeNode, currDepth: number) {
        this.maxDepthFound = Math.max(this.maxDepthFound, currDepth)
        if (node.left !== null) {
            this.findMaxDepth(node.left, currDepth + 1)
        }
        if (node.right !== null) {
            this.findMaxDepth(node.right, currDepth + 1)
        }
    }
}
