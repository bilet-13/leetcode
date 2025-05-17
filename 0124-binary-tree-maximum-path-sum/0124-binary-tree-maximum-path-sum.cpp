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
private:
    int maxPath = INT_MIN;
    int getMaxPath(TreeNode *root) {
        if (root == nullptr) {
            return 0;
        }

        auto left = max(getMaxPath(root->left), 0);
        auto right = max(getMaxPath(root->right), 0);

        auto fullPath = root->val + left + right;

        maxPath = max(maxPath, fullPath);

        return max(root->val + left, root->val + right);
    }
public:
    int maxPathSum(TreeNode* root) {
        getMaxPath(root);
        return maxPath;
    }
};
