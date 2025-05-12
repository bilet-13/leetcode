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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        queue<TreeNode*> nodes;
        TreeNode *rightestNode;

        if (root != nullptr) {
            nodes.push(root);
        }

        while (!nodes.empty()) {
            auto size = nodes.size();

            for (int i = 0; i < size; i++) {
                auto node = nodes.front();
                nodes.pop();

                if (node->left != nullptr) {
                    nodes.push(node->left);
                }
                if(node->right != nullptr) {
                    nodes.push(node->right);
                }
                rightestNode = node;
            }
            result.push_back(rightestNode->val);
        }
        return result;
    }
};
