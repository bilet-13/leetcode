/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == NULL){
            return head;
        }

        unordered_map<Node*, Node*> new_nodes;

        Node* new_head = new Node(head->val);
        Node* cur = head;
        Node* new_cur = new_head;
        new_nodes[cur] = new_cur;

        while (cur->next != NULL){
            cur = cur->next;
            new_cur->next = new Node(cur->val);
            new_cur = new_cur->next;
            new_nodes[cur] = new_cur;
        }

        cur = head;
        new_cur = new_head;

        while(cur != NULL){
            new_cur->random = new_nodes[cur->random];
            cur = cur->next;
            new_cur = new_cur->next;
        }
        
        return new_head;
    }
};