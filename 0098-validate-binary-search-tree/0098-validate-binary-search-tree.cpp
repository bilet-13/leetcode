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
    bool isValidBST(TreeNode* root) {
        vector<int> nodes;
        inOrderTravsal(root, nodes);

        int previous = nodes[0];

        for (int i = 1; i < nodes.size(); i++) {
            if (nodes[i] <= previous) {
                return false;
            }
            previous = nodes[i];
        }
        return true;
    }

    void inOrderTravsal(TreeNode* root, vector<int>& nodes) {
        if (root == nullptr) {
            return;
        }
        inOrderTravsal(root->left, nodes);

        nodes.push_back(root->val);

        inOrderTravsal(root->right, nodes);
    }
};
