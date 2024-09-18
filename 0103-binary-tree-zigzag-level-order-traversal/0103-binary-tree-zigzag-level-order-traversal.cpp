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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if(!root){
            return {};
        }

        queue<TreeNode*> nodes;
        vector<vector<int>> levels;
        int depth = 0;

        nodes.push(root);
        while(!nodes.empty()){
            vector<TreeNode*> next_nodes;
            vector<TreeNode*> level_nodes;
            levels.push_back({});

            while(!nodes.empty()){
                auto cur = nodes.front();
                nodes.pop();
                levels[depth].push_back(cur->val);
                level_nodes.push_back(cur);
            }

            reverse(level_nodes.begin(), level_nodes.end());
            depth += 1;
            for(int i = 0; i < level_nodes.size(); i++){
               if (depth % 2 == 1){
                    if(level_nodes[i]->right) next_nodes.push_back(level_nodes[i]->right);
                    if(level_nodes[i]->left) next_nodes.push_back(level_nodes[i]->left);
               }
               else{
                    if(level_nodes[i]->left) next_nodes.push_back(level_nodes[i]->left);
                    if(level_nodes[i]->right) next_nodes.push_back(level_nodes[i]->right);
               }
            }
            
            for(int i = 0; i < next_nodes.size(); i++){
                nodes.push(next_nodes[i]);
            }
        }
        return levels;
    }
};