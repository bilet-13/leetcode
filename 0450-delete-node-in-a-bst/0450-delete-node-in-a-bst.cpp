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

        auto pos = find_key(root, key);
        if(pos.second == nullptr){
            return root;
        }
        
        auto parent = pos.first;
        auto node = pos.second;
        bool left = parent != nullptr && parent->left == node ? true : false;

        if(node->left == nullptr && node->right == nullptr){
            if (parent == nullptr){
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

        else if (node->left == nullptr || node->right == nullptr){
            auto remain_node = node->left != nullptr ? node->left : node->right;
            if (parent == nullptr){
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
            auto largest_left_subtree = find_largest(node->left);
            auto replace_val = largest_left_subtree->val;

            deleteNode(node, replace_val);

            node->val = replace_val;
            return root;
        }
    }

    TreeNode* find_largest(TreeNode* root){
        if(root->right == nullptr){
            return root;
        }
        return find_largest(root->right);
    }

    pair<TreeNode*, TreeNode*> find_key(TreeNode* root, int key){
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
        
        auto left_result = find_key(root->left, key);
        if (left_result.second != nullptr){
            return left_result;
        }

        return find_key(root->right, key);
    }
};