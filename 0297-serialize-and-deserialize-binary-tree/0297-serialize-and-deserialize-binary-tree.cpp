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

class Codec {
private: 
    void serializeHelper(TreeNode *root, stringstream &ss) {
        if (root == nullptr) {
            ss << "#,";
            return;
        }

        ss << root->val << ",";

        serializeHelper(root->left, ss);
        serializeHelper(root->right, ss);

    }

    TreeNode* deserializeHelper(queue<string> &nodes) {
        if (nodes.empty()) {
            return nullptr;
        }

        string node = nodes.front();
        nodes.pop();

        if (node == "#") {
            return nullptr;
        }

        auto root = new TreeNode(stoi(node));
        root->left = deserializeHelper(nodes);
        root->right = deserializeHelper(nodes);
        return root;
    }

public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        stringstream ss;
        serializeHelper(root, ss);

        string result = ss.str();

        result.pop_back();
        return result;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        stringstream ss(data);
        queue<string> nodes;
        string node;

        while (getline(ss, node, ',')) {
            nodes.push(node);
        }

        return deserializeHelper(nodes);
    }
};
