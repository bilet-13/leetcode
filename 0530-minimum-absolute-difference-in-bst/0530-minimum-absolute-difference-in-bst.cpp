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
    void inorderTraverse(TreeNode* root, vector<int>& sorted_list){
        if (!root){
            return;
        }

        inorderTraverse(root->left, sorted_list);
        
        sorted_list.push_back(root->val);
        
        inorderTraverse(root->right, sorted_list);
        return;
    }

public:
    int getMinimumDifference(TreeNode* root) {
        
        vector<int> sorted_list;

        inorderTraverse(root, sorted_list);
        int min_difference = INT_MAX;
        int prev = sorted_list[0];
        int difference;

        for(auto i = 1; i < sorted_list.size(); i++){
            difference = abs(sorted_list[i] - prev);
            min_difference = min(min_difference, difference);
            
            prev = sorted_list[i];
        }
        return min_difference;


    }
};