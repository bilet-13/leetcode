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

        vector<int> answer_nodes;
        queue< pair<TreeNode*, int> > nodeLevelQueue;
        vector< pair<TreeNode*, int> > nodeLevelVec;

        if(root == NULL){
            return answer_nodes;
        }
        nodeLevelQueue.push(make_pair(root, 0));

        while(!nodeLevelQueue.empty()){

            pair<TreeNode*, int> tmp_nodeLevel;

            tmp_nodeLevel = nodeLevelQueue.front();
            nodeLevelQueue.pop();

            nodeLevelVec.push_back(tmp_nodeLevel);

            if(tmp_nodeLevel.first != NULL){
                nodeLevelQueue.push(make_pair(tmp_nodeLevel.first->right, 
                                     tmp_nodeLevel.second + 1));
                nodeLevelQueue.push(make_pair(tmp_nodeLevel.first->left, 
                                     tmp_nodeLevel.second + 1));
            }
        }

        int level = -1;

        for(vector< pair<TreeNode*, int> >::iterator it = nodeLevelVec.begin(); it != nodeLevelVec.end(); it++){
            if(it->second > level && it->first != NULL){
                answer_nodes.push_back(it->first->val);
                level++;
            }
        }
        return answer_nodes;
    }
};