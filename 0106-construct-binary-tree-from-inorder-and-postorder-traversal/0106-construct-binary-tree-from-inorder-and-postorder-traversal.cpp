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
    unordered_map<int, int> indices;

    void _buildIndices(vector<int>& inorder){
        for(int i = 0; i < inorder.size(); i++){
            indices[inorder[i]] = i;
        }
    }

    TreeNode* _buildTree(vector<int>& inorder, vector<int>& postorder, int i_start, int i_end,int p_start, int p_end){
        if(i_start <= i_end){
            int val = postorder[p_end];
            auto node = new TreeNode(val);

            if(i_start < i_end){
                int i = indices[val];
                int left_size = i - i_start;
                node->left = _buildTree(inorder, postorder, i_start, i_start+left_size-1, p_start, p_start+left_size-1);
                node->right = _buildTree(inorder, postorder, i+1, i_end, p_start+left_size, p_end-1);
            }
            return node;
        }
        
        return nullptr;
    }
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        _buildIndices(inorder);
        return _buildTree(inorder, postorder, 0, inorder.size()-1, 0, postorder.size()-1);
    }
};