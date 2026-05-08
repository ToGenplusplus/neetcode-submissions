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

    result: number = 0
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    diameterOfBinaryTree(root: TreeNode | null) {
        /**
         for a given node, the # of edges in the node is
         the height of the left subtree + the height of the right subtree

         using the 1st example on the left
         node 5 has height of 0
         node 3 has height of 1
         node 4 has height of 0
         
         node 2 height = 
         max (left subtree, right subtree)
         node 2 diameter = left (2) + right (1)
         */
        this.findHeight(root)
        return this.result
    }

    findHeight(node: TreeNode | null): number {
        if (node === null) return 0

        let left = this.findHeight(node.left)
        let right = this.findHeight(node.right) 

        this.result = Math.max(this.result, left + right)

        return 1 + Math.max(left, right)
    }
}
