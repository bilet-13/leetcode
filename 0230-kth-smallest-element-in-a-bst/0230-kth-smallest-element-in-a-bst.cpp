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
    int kthSmallest(TreeNode* root, int k) {
        vector<int> values;
        inOrder(root, values);

        return values[k - 1];
    }

    void inOrder(TreeNode *root, vector<int>& values) {
        if (root == nullptr) {
            return;
        }

        inOrder(root->left, values);

        values.push_back(root->val);

        inOrder(root->right, values);
    }
};
