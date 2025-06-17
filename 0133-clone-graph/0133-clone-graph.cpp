/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) {
            return nullptr;
        }
        unordered_map<int, Node*> copiedNodes;

        unordered_set<int> visited;
        stack<Node*> nodes;

        nodes.push(node);

        while (!nodes.empty()) {
            auto *node = nodes.top();
            nodes.pop();
            if (visited.find(node->val) != visited.end()) {
                continue;
            }

            visited.insert(node->val);

            if (copiedNodes.find(node->val) == copiedNodes.end()) {
                copiedNodes[node->val] = new Node(node->val);
            }

            for (auto &neighbor: node->neighbors) {
                if (visited.find(neighbor->val) == visited.end()) {
                    nodes.push(neighbor);
                }
                if (copiedNodes.find(neighbor->val) == copiedNodes.end()) {
                    copiedNodes[neighbor->val] = new Node(neighbor->val);
                }
                copiedNodes[node->val]->neighbors.push_back(copiedNodes[neighbor->val]);
            }            
                    
        }
        return copiedNodes[node->val];
    } 
};
