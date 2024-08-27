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
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (root == nullptr){
            return root;
        }

        auto pos = findKey(root, key);
        if(pos.second == nullptr){
            return root;
        }
        
        auto parent = pos.first;
        auto node = pos.second;
        bool left = parent && parent->left == node ;

        if(!node->left && !node->right){
            if (!parent){
                return nullptr;
            }

            if (left){
                parent->left = nullptr;
            }
            else{
                parent->right = nullptr;
            }
            return root;
        }

        else if (!node->left  || !node->right ){
            auto remain_node = node->left ? node->left : node->right;
            if (!parent){
                return remain_node;
            }
        
            if (left) {
                parent->left = remain_node;
            }
            else{
                parent->right = remain_node;
            }
            return root;
        }

        else{
            auto largest_left_subtree = findLargest(node->left);
            auto replace_val = largest_left_subtree->val;

            deleteNode(node, replace_val);

            node->val = replace_val;
            return root;
        }
    }

    TreeNode* findLargest(TreeNode* root){
        if(root->right == nullptr){
            return root;
        }
        return findLargest(root->right);
    }

    pair<TreeNode*, TreeNode*> findKey(TreeNode* root, int key){
        if (root == nullptr){
            return make_pair(nullptr, nullptr);
        }

        if (root->val == key){
            return make_pair(nullptr, root);
        }

        if (root->left != nullptr && root->left->val == key){
            return make_pair(root, root->left);
        }

        else if (root->right != nullptr && root->right->val == key){
            return make_pair(root, root->right);
        }
        
        auto left_result = findKey(root->left, key);
        if (left_result.second != nullptr){
            return left_result;
        }

        return findKey(root->right, key);
    }
};