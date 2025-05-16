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
unordered_map<int, int> inorderValueToIndex;

public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for (int i = 0; i < inorder.size(); i++) {
            inorderValueToIndex[inorder[i]] = i;
        }

       return buildBinaryTree(preorder, 0, preorder.size(), inorder, 0, inorder.size());
    }

    TreeNode *buildBinaryTree(vector<int>& preorder, int preorderStart, int preorderEnd, vector<int>& inorder, int inorderStart, int inorderEnd) {
        if (preorderStart >= preorderEnd) {
            return nullptr;
        }

        auto root = new TreeNode(preorder[preorderStart]);

        int rootInorderIndex = inorderValueToIndex[preorder[preorderStart]];

        int leftSize = rootInorderIndex - inorderStart;
        int leftStart = preorderStart + 1;
        root->left = buildBinaryTree(preorder, leftStart, leftStart + leftSize, inorder, inorderStart, inorderStart + leftSize);
        root->right = buildBinaryTree(preorder, leftStart + leftSize, preorderEnd, inorder, inorderStart + leftSize + 1, inorderEnd);

        return root;
    }
};
