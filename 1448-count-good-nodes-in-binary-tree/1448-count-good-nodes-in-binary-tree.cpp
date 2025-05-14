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
    int goodNodes(TreeNode* root) {
        int max_parent = INT_MIN;
        return findGoodNodes(root, max_parent);
    }

    int findGoodNodes(TreeNode* root, int max_parent) {
        if (root == nullptr) {
            return 0;
        }

        bool isGoodNode = root->val >= max_parent ? true : false;
        max_parent = max(root->val, max_parent);
        
        int leftCount = findGoodNodes(root->left, max_parent);
        int rightCount = findGoodNodes(root->right, max_parent);

        return  (isGoodNode ? 1 : 0) + leftCount + rightCount;
    }
};
