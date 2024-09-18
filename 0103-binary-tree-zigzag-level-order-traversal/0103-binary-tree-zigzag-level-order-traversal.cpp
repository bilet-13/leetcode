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
                auto* first = depth % 2 == 0 ? level_nodes[i]->left : level_nodes[i]->right;
                auto* second = depth % 2 == 0 ? level_nodes[i]->right : level_nodes[i]->left;

                if (first) next_nodes.push_back(first);
                if (second) next_nodes.push_back(second);
            }

            for(int i = 0; i < next_nodes.size(); i++){
                nodes.push(next_nodes[i]);
            }
        }
        return levels;
    }
};