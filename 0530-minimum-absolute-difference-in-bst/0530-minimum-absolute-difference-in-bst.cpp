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
    int getMinimumDifference(TreeNode* root) {
        
        if (!root){
            return INT_MAX;
        }

        if(!root->left && !root->right){
            return INT_MAX;
        }
        else if(!root->left){
            auto successor_val = get_successor(root);
            return min(abs(root->val - successor_val), getMinimumDifference(root->right));
        }
        else if(!root->right){
            auto predecessor_val = get_predecessor(root);
            return min(abs(root->val - predecessor_val), getMinimumDifference(root->left));
        }

        else{
            auto successor_val = get_successor(root);
            auto predecessor_val = get_predecessor(root);
            
            auto min_root_difference = min(abs(root->val - predecessor_val), abs(root->val - successor_val));
            auto min_difference_two_sbutree = min(getMinimumDifference(root->left), getMinimumDifference(root->right));
            
            return min(min_root_difference, min_difference_two_sbutree); 
        }
    }

    int get_predecessor(TreeNode* root){
        auto node = root->left;

        while(node && node->right){
            node = node->right;
        }
        return node->val;
    }

    int get_successor(TreeNode* root){
        auto node = root->right;

        while(node && node->left){
            node = node->left;
        }
        return node->val;
    }

};