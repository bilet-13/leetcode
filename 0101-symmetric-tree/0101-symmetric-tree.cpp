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
    bool isSymmetric(TreeNode* root) {
        return recursiveCheck(root->left, root->right);
    }
private:
    bool recursiveCheck(TreeNode* node1, TreeNode* node2){
        if (node1 == NULL and node2 == NULL){
            return true;
        }
        else if (node1== NULL or node2 == NULL){
            return false;
        }
        if(node1->val == node2->val){
            return (recursiveCheck(node1->left, node2->right) &&
                    recursiveCheck(node1->right, node2->left) );
        }
        else{
            return false;
        }
    }
};