/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int best = 0;
        depth(root, best);
        return best;
    }

private:
    int depth(TreeNode* node, int& best) {
        if (!node) return 0;
        int left  = depth(node->left, best);
        int right = depth(node->right, best);
        best = max(best, left + right);   // path bending at this node
        return 1 + max(left, right);      // height, for the parent
    }
};