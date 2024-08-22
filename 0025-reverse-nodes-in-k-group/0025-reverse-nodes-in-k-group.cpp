/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {

        auto node = head;
        auto dummy = new ListNode(-1, head);
        auto prev = dummy;
        stack<ListNode*> reverse_nodes;

        while(node != nullptr){
            reverse_nodes.push(node);
            node = node->next;

            if(reverse_nodes.size() < k){
                continue;
            }
            else{
                ListNode* reverse_head = reverse_nodes.top();
                reverse_nodes.pop();
                auto prev_reverse_node =  reverse_head;

                while(!reverse_nodes.empty()){
                    auto reverse_node = reverse_nodes.top();
                    reverse_nodes.pop();
                    prev_reverse_node->next = reverse_node;
                    prev_reverse_node = prev_reverse_node->next;
                }
                prev->next = reverse_head;
                prev_reverse_node->next = node;
                prev = prev_reverse_node;
            }
            
        }
        return dummy->next;
    }
};